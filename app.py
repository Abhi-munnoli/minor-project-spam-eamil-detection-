import os
import re
import time

from datetime import datetime, timezone
from pathlib import Path
from functools import wraps

import joblib
import firebase_admin
from firebase_admin import credentials, firestore, auth as firebase_auth

from flask import (
    Flask,
    jsonify,
    render_template,
    request,
    session,
    redirect,
    url_for
)

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from dotenv import load_dotenv

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


# ============================================================
# BASE CONFIGURATION
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

load_dotenv(BASE_DIR / ".env")


app = Flask(__name__)

# Flask secret key
app.secret_key = os.getenv(
    "https://spam-email-detector-ab164-default-rtdb.firebaseio.com/",
    "change-this-secret-key"
)

# Session security
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
app.config["SESSION_COOKIE_SECURE"] = (
    os.getenv("SESSION_COOKIE_SECURE", "false").lower() == "true"
)

# Maximum request size
app.config["MAX_CONTENT_LENGTH"] = 1 * 1024 * 1024


# ============================================================
# RATE LIMITER
# ============================================================

limiter = Limiter(
    key_func=get_remote_address,
    app=app,
    default_limits=["200 per hour"]
)


# ============================================================
# MACHINE LEARNING MODEL
# ============================================================

MODEL_PATH = BASE_DIR / "model" / "spam_model.pkl"
VECTORIZER_PATH = BASE_DIR / "model" / "vectorizer.pkl"

MAX_MESSAGE_LENGTH = int(
    os.getenv("MAX_MESSAGE_LENGTH", "10000")
)

model = None
vectorizer = None
MODEL_ERROR = None

try:
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)

    print("========================================")
    print("SpamShield AI ML Model Loaded")
    print("========================================")

except Exception as exc:
    MODEL_ERROR = (
        "ML model is not ready. "
        "Run 'python train_model.py'. "
        f"Details: {exc}"
    )

    print("MODEL ERROR:")
    print(MODEL_ERROR)


# ============================================================
# FIREBASE / FIRESTORE
# ============================================================

db = None
FIREBASE_ERROR = None

try:

    if not firebase_admin._apps:

        service_path = BASE_DIR / "serviceAccountKey.json"

        if not service_path.exists():
            raise FileNotFoundError(
                "serviceAccountKey.json is missing."
            )

        cred = credentials.Certificate(
            str(service_path)
        )

        firebase_admin.initialize_app(cred)

    db = firestore.client()

    print("========================================")
    print("Firebase / Firestore Connected")
    print("========================================")

except Exception as exc:

    FIREBASE_ERROR = str(exc)

    print("FIREBASE ERROR:")
    print(FIREBASE_ERROR)


# ============================================================
# NLTK
# ============================================================

try:

    nltk.data.find("corpora/stopwords")

    STOPWORDS = set(
        stopwords.words("english")
    )

except LookupError:

    # Offline-safe fallback
    STOPWORDS = {
        "a",
        "an",
        "and",
        "are",
        "as",
        "at",
        "be",
        "by",
        "for",
        "from",
        "has",
        "have",
        "he",
        "her",
        "his",
        "i",
        "in",
        "is",
        "it",
        "its",
        "me",
        "my",
        "of",
        "on",
        "or",
        "our",
        "she",
        "that",
        "the",
        "their",
        "them",
        "there",
        "they",
        "this",
        "to",
        "was",
        "we",
        "were",
        "what",
        "when",
        "where",
        "which",
        "who",
        "will",
        "with",
        "you",
        "your"
    }


STEMMER = PorterStemmer()


# ============================================================
# TEXT CLEANING
# ============================================================

def clean_text(text):

    text = str(text).lower()

    # Replace URLs
    text = re.sub(
        r"http\S+|www\S+",
        " URL ",
        text
    )

    # Replace email addresses
    text = re.sub(
        r"\S+@\S+",
        " EMAIL ",
        text
    )

    # Keep alphabetic characters and spaces
    text = re.sub(
        r"[^a-zA-Z\s]",
        " ",
        text
    )

    tokens = [
        STEMMER.stem(word)
        for word in text.split()
        if word not in STOPWORDS
        and len(word) > 1
    ]

    return " ".join(tokens)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def firebase_ready():
    return db is not None


def get_admin_emails():

    return {
        email.strip().lower()
        for email in os.getenv(
            "ADMIN_EMAILS",
            ""
        ).split(",")
        if email.strip()
    }


def login_required(view):

    @wraps(view)
    def wrapped(*args, **kwargs):

        if not session.get("uid"):

            if request.path.startswith("/api/"):

                return jsonify({
                    "success": False,
                    "error": "Authentication required."
                }), 401

            return redirect(
                url_for("login")
            )

        return view(*args, **kwargs)

    return wrapped


def admin_required(view):

    @wraps(view)
    def wrapped(*args, **kwargs):

        if not session.get("uid"):

            return jsonify({
                "success": False,
                "error": "Authentication required."
            }), 401

        if session.get("role") != "admin":

            return jsonify({
                "success": False,
                "error": "Administrator access required."
            }), 403

        return view(*args, **kwargs)

    return wrapped


def user_record(uid):

    if not db:
        return {}

    doc = (
        db.collection("users")
        .document(uid)
        .get()
    )

    return (
        doc.to_dict()
        if doc.exists
        else {}
    )


# ============================================================
# FIREBASE WEB CONFIG
# ============================================================

@app.context_processor
def inject_config():

    return {
        "firebase_config": {

            "apiKey": os.getenv(
                "FIREBASE_WEB_API_KEY",
                ""
            ),

            "authDomain": os.getenv(
                "FIREBASE_AUTH_DOMAIN",
                ""
            ),

            "projectId": os.getenv(
                "FIREBASE_PROJECT_ID",
                ""
            ),

            "storageBucket": os.getenv(
                "FIREBASE_STORAGE_BUCKET",
                ""
            ),

            "messagingSenderId": os.getenv(
                "FIREBASE_MESSAGING_SENDER_ID",
                ""
            ),

            "appId": os.getenv(
                "FIREBASE_APP_ID",
                ""
            ),
        },

        "model_ready": (
            model is not None
            and vectorizer is not None
        ),
    }


# ============================================================
# PAGE ROUTES
# ============================================================

@app.route("/")
def index():

    return render_template(
        "index.html"
    )


@app.route("/login")
def login():

    if session.get("uid"):

        return redirect(
            url_for("dashboard")
        )

    return render_template(
        "login.html"
    )


@app.route("/register")
def register():

    if session.get("uid"):

        return redirect(
            url_for("dashboard")
        )

    return render_template(
        "register.html"
    )


@app.route("/dashboard")
@login_required
def dashboard():

    return render_template(
        "dashboard.html"
    )


@app.route("/history")
@login_required
def history():

    return render_template(
        "history.html"
    )


@app.route("/profile")
@login_required
def profile():

    return render_template(
        "profile.html"
    )


@app.route("/admin")
@login_required
def admin():

    if session.get("role") != "admin":

        return redirect(
            url_for("dashboard")
        )

    return render_template(
        "admin.html"
    )


# ============================================================
# FIREBASE LOGIN → FLASK SESSION
# ============================================================

@app.post("/api/session")
@limiter.limit("30 per minute")
def create_session():

    data = request.get_json(
        silent=True
    ) or {}

    token = str(
        data.get("idToken", "")
    ).strip()

    print("\n========================================")
    print("LOGIN SESSION REQUEST")
    print("========================================")

    if not token:

        print("ERROR: Firebase ID token missing.")

        return jsonify({
            "success": False,
            "error": "Missing Firebase ID token."
        }), 400

    try:

        # Verify Firebase token using Admin SDK
        decoded = firebase_auth.verify_id_token(
            token
        )

        uid = decoded.get("uid")

        email = (
            decoded.get("email")
            or ""
        ).lower().strip()

        name = (
            decoded.get("name")
            or email.split("@")[0]
            or "User"
        )

        if not uid:

            raise ValueError(
                "Firebase token does not contain UID."
            )

        # Determine role
        role = (
            "admin"
            if email in get_admin_emails()
            else "user"
        )

        # ====================================================
        # CREATE / UPDATE FIRESTORE USER
        # ====================================================

        if db:

            ref = (
                db.collection("users")
                .document(uid)
            )

            snap = ref.get()

            if not snap.exists:

                ref.set({
                    "uid": uid,
                    "name": name,
                    "email": email,
                    "created_at":
                        firestore.SERVER_TIMESTAMP,
                    "role": role
                })

                print(
                    "New Firestore user created:",
                    email
                )

            else:

                existing = (
                    snap.to_dict()
                    or {}
                )

                # Preserve existing role
                role = existing.get(
                    "role",
                    role
                )

                # Keep basic user information current
                ref.set({
                    "uid": uid,
                    "name": name,
                    "email": email
                }, merge=True)

        # ====================================================
        # CREATE FLASK SESSION
        # ====================================================

        session.clear()

        session["uid"] = uid
        session["email"] = email
        session["name"] = name
        session["role"] = role
        session.permanent = True

        print("Flask session created successfully.")
        print("UID:", uid)
        print("Email:", email)
        print("Role:", role)

        return jsonify({
            "success": True,
            "message": "Login successful.",
            "user": {
                "uid": uid,
                "email": email,
                "name": name,
                "role": role
            }
        })

    except Exception as exc:

        print("\n========================================")
        print("FIREBASE SESSION ERROR")
        print("========================================")
        print(repr(exc))

        return jsonify({
            "success": False,
            "error":
                "Firebase authentication could not be verified.",
            "details":
                str(exc)
            if os.getenv(
                "FLASK_ENV"
            ) == "development"
            else None
        }), 401


# ============================================================
# LOGOUT
# ============================================================

@app.post("/api/logout")
def api_logout():

    session.clear()

    return jsonify({
        "success": True,
        "message": "Logged out successfully."
    })


# ============================================================
# CURRENT USER
# ============================================================

@app.get("/api/me")
@login_required
def me():

    return jsonify({

        "success": True,

        "user": {
            "uid": session.get("uid"),
            "email": session.get("email"),
            "name": session.get("name"),
            "role": session.get("role")
        }

    })


# ============================================================
# SPAM PREDICTION
# ============================================================

@app.post("/api/predict")
@login_required
@limiter.limit("30 per minute")
def predict():

    started = time.perf_counter()

    if model is None or vectorizer is None:

        return jsonify({
            "success": False,
            "error": MODEL_ERROR
        }), 503

    data = request.get_json(
        silent=True
    ) or {}

    message = str(
        data.get("message", "")
    ).strip()

    if not message:

        return jsonify({
            "success": False,
            "error":
                "Please enter a message to analyze."
        }), 400

    if len(message) > MAX_MESSAGE_LENGTH:

        return jsonify({
            "success": False,
            "error":
                f"Message exceeds "
                f"{MAX_MESSAGE_LENGTH} characters."
        }), 400

    try:

        clean = clean_text(
            message
        )

        features = vectorizer.transform(
            [clean]
        )

        prediction = model.predict(
            features
        )[0]

        probabilities = model.predict_proba(
            features
        )[0]

        confidence = float(
            max(probabilities) * 100
        )

        label = (
            "Spam"
            if prediction == "spam"
            else "Not Spam"
        )

        elapsed_ms = round(
            (
                time.perf_counter()
                - started
            ) * 1000,
            2
        )

        # ====================================================
        # FIRESTORE STORAGE
        # ====================================================

        if db:

            db.collection(
                "predictions"
            ).add({

                "user_id":
                    session["uid"],

                "email_text":
                    message,

                "prediction":
                    label,

                "confidence":
                    confidence,

                "timestamp":
                    firestore.SERVER_TIMESTAMP,

                "analysis_ms":
                    elapsed_ms
            })

            db.collection(
                "activity_logs"
            ).add({

                "user_id":
                    session["uid"],

                "action":
                    f"Analyzed message as {label}",

                "timestamp":
                    firestore.SERVER_TIMESTAMP,

                "ip_address":
                    request.headers.get(
                        "X-Forwarded-For",
                        request.remote_addr
                    )
            })

        return jsonify({

            "success": True,

            "prediction":
                label,

            "confidence":
                round(
                    confidence,
                    2
                ),

            "message_length":
                len(message),

            "analysis_ms":
                elapsed_ms,

            "analyzed_at":
                datetime.now(
                    timezone.utc
                ).isoformat()
        })

    except Exception as exc:

        print(
            "Prediction error:",
            repr(exc)
        )

        return jsonify({
            "success": False,
            "error":
                "Unable to analyze the message."
        }), 500


# ============================================================
# HISTORY
# ============================================================

@app.get("/api/history")
@login_required
def api_history():

    if not db:

        return jsonify({
            "success": False,
            "error":
                "Firestore is not configured."
        }), 503

    try:

        requested_limit = int(
            request.args.get(
                "limit",
                100
            )
        )

        limit = min(
            max(requested_limit, 1),
            200
        )

    except ValueError:

        limit = 100

    docs = (
        db.collection("predictions")
        .where(
            "user_id",
            "==",
            session["uid"]
        )
        .stream()
    )

    items = []

    for doc in docs:

        data = doc.to_dict()

        timestamp_value = (
            data.get("timestamp")
        )

        timestamp = (
            timestamp_value.isoformat()
            if hasattr(
                timestamp_value,
                "isoformat"
            )
            else None
        )

        items.append({

            "id":
                doc.id,

            "message":
                data.get(
                    "email_text",
                    ""
                ),

            "preview":
                data.get(
                    "email_text",
                    ""
                )[:100],

            "prediction":
                data.get(
                    "prediction",
                    ""
                ),

            "confidence":
                round(
                    float(
                        data.get(
                            "confidence",
                            0
                        )
                    ),
                    2
                ),

            "timestamp":
                timestamp,

            "analysis_ms":
                data.get(
                    "analysis_ms",
                    0
                )
        })

    items.sort(
        key=lambda item:
            item["timestamp"] or "",
        reverse=True
    )

    return jsonify({
        "success": True,
        "items": items[:limit]
    })


# ============================================================
# DELETE HISTORY ITEM
# ============================================================

@app.delete("/api/history/<doc_id>")
@login_required
def delete_history(doc_id):

    if not db:

        return jsonify({
            "success": False,
            "error":
                "Firestore is not configured."
        }), 503

    ref = (
        db.collection("predictions")
        .document(doc_id)
    )

    doc = ref.get()

    if not doc.exists:

        return jsonify({
            "success": False,
            "error":
                "Record not found."
        }), 404

    data = doc.to_dict()

    if data.get(
        "user_id"
    ) != session["uid"]:

        return jsonify({
            "success": False,
            "error":
                "Record not found."
        }), 404

    ref.delete()

    return jsonify({
        "success": True,
        "message":
            "Prediction deleted."
    })


# ============================================================
# USER STATISTICS
# ============================================================

@app.get("/api/stats")
@login_required
def stats():

    if not db:

        return jsonify({
            "success": False,
            "error":
                "Firestore is not configured."
        }), 503

    docs = list(
        db.collection(
            "predictions"
        )
        .where(
            "user_id",
            "==",
            session["uid"]
        )
        .stream()
    )

    total = len(docs)

    spam = sum(
        1
        for doc in docs
        if doc.to_dict().get(
            "prediction"
        ) == "Spam"
    )

    safe = total - spam

    rate = (
        round(
            (spam / total) * 100,
            1
        )
        if total
        else 0
    )

    return jsonify({

        "success": True,

        "stats": {

            "total":
                total,

            "spam":
                spam,

            "safe":
                safe,

            "rate":
                rate
        }
    })


# ============================================================
# UPDATE PROFILE
# ============================================================

@app.put("/api/profile")
@login_required
def update_profile():

    data = request.get_json(
        silent=True
    ) or {}

    name = str(
        data.get(
            "name",
            ""
        )
    ).strip()

    if not name or len(name) > 80:

        return jsonify({
            "success": False,
            "error":
                "Enter a valid name."
        }), 400

    session["name"] = name

    if db:

        db.collection(
            "users"
        ).document(
            session["uid"]
        ).set(
            {
                "name": name
            },
            merge=True
        )

    return jsonify({
        "success": True,
        "name": name
    })


# ============================================================
# ADMIN STATISTICS
# ============================================================

@app.get("/api/admin/stats")
@admin_required
def admin_stats():

    if not db:

        return jsonify({
            "success": False,
            "error":
                "Firestore is not configured."
        }), 503

    users = list(
        db.collection(
            "users"
        ).stream()
    )

    predictions = list(
        db.collection(
            "predictions"
        ).stream()
    )

    spam = sum(
        1
        for doc in predictions
        if doc.to_dict().get(
            "prediction"
        ) == "Spam"
    )

    safe = (
        len(predictions)
        - spam
    )

    rate = (
        round(
            (spam / len(predictions))
            * 100,
            1
        )
        if predictions
        else 0
    )

    return jsonify({

        "success": True,

        "stats": {

            "users":
                len(users),

            "predictions":
                len(predictions),

            "spam":
                spam,

            "safe":
                safe,

            "rate":
                rate
        }
    })


# ============================================================
# ADMIN USERS
# ============================================================

@app.get("/api/admin/users")
@admin_required
def admin_users():

    if not db:

        return jsonify({
            "success": False,
            "error":
                "Firestore is not configured."
        }), 503

    items = []

    for doc in (
        db.collection(
            "users"
        ).stream()
    ):

        data = doc.to_dict()

        items.append({

            "uid":
                data.get(
                    "uid",
                    doc.id
                ),

            "name":
                data.get(
                    "name",
                    ""
                ),

            "email":
                data.get(
                    "email",
                    ""
                ),

            "role":
                data.get(
                    "role",
                    "user"
                )
        })

    return jsonify({
        "success": True,
        "items": items
    })


# ============================================================
# REQUEST TOO LARGE
# ============================================================

@app.errorhandler(413)
def too_large(_):

    return jsonify({
        "success": False,
        "error":
            "Request is too large."
    }), 413


# ============================================================
# GLOBAL ERROR HANDLER
# ============================================================

@app.errorhandler(500)
def internal_error(error):

    print(
        "Internal server error:",
        repr(error)
    )

    return jsonify({
        "success": False,
        "error":
            "Internal server error."
    }), 500


# ============================================================
# START SERVER
# ============================================================

if __name__ == "__main__":

    print("\n========================================")
    print("        SPAMSHIELD AI SERVER")
    print("========================================")
    print("Server: http://127.0.0.1:5000")
    print(
        "ML Model:",
        "READY"
        if model is not None
        else "NOT READY"
    )
    print(
        "Firebase:",
        "CONNECTED"
        if db is not None
        else "NOT CONNECTED"
    )
    print("========================================\n")

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=(
            os.getenv(
                "FLASK_ENV",
                "development"
            ).lower()
            == "development"
        )
    )