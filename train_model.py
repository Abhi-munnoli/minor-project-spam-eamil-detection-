import re
from pathlib import Path
import joblib
import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.model_selection import train_test_split

BASE_DIR = Path(__file__).resolve().parent
DATASET = BASE_DIR / "dataset" / "spam.csv"
MODEL_DIR = BASE_DIR / "model"
MODEL_PATH = MODEL_DIR / "spam_model.pkl"
VECTORIZER_PATH = MODEL_DIR / "vectorizer.pkl"

def ensure_nltk():
    try:
        stopwords.words("english")
        return set(stopwords.words("english"))
    except LookupError:
        # Offline-safe fallback. NLTK is still used for stemming.
        return {
            "a","an","and","are","as","at","be","by","for","from","has","have","he",
            "her","his","i","in","is","it","its","me","my","of","on","or","our",
            "she","that","the","their","them","there","they","this","to","was","we",
            "were","what","when","where","which","who","will","with","you","your"
        }

STOPWORDS = ensure_nltk()
STEMMER = PorterStemmer()

def clean_text(text: str) -> str:
    text = str(text).lower()
    text = re.sub(r"http\S+|www\S+", " URL ", text)
    text = re.sub(r"\S+@\S+", " EMAIL ", text)
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    tokens = [STEMMER.stem(w) for w in text.split() if w not in STOPWORDS and len(w) > 1]
    return " ".join(tokens)

def load_dataset():
    if not DATASET.exists():
        raise FileNotFoundError(f"Dataset not found: {DATASET}")
    df = pd.read_csv(DATASET)
    if df.empty:
        raise ValueError("Dataset is empty.")
    cols = {c.lower().strip(): c for c in df.columns}
    label_col = next((cols[k] for k in ("label", "category", "class", "target", "v1") if k in cols), None)
    text_col = next((cols[k] for k in ("message", "text", "email", "body", "v2") if k in cols), None)
    if not label_col or not text_col:
        raise ValueError("Could not detect label/text columns. Expected label/category/class and message/text/email/body columns.")
    data = df[[label_col, text_col]].dropna().copy()
    data.columns = ["label", "message"]
    data["label"] = data["label"].astype(str).str.strip().str.lower()
    data["message"] = data["message"].astype(str)
    data["label"] = data["label"].map(lambda x: "spam" if x in {"spam", "1", "junk"} else "ham")
    data["clean"] = data["message"].map(clean_text)
    data = data[data["clean"].str.len() > 0]
    if data["label"].nunique() < 2:
        raise ValueError("Dataset must contain both spam and ham examples.")
    return data

def main():
    print("=== SpamShield AI model training ===")
    df = load_dataset()
    X_train, X_test, y_train, y_test = train_test_split(
        df["clean"], df["label"], test_size=0.25, random_state=42, stratify=df["label"]
    )
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), min_df=1, max_df=0.98, sublinear_tf=True)
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    model = LogisticRegression(max_iter=1000, class_weight="balanced", random_state=42)
    model.fit(X_train_vec, y_train)
    pred = model.predict(X_test_vec)

    print(f"Accuracy : {accuracy_score(y_test, pred):.4f}")
    print(f"Precision: {precision_score(y_test, pred, pos_label='spam', zero_division=0):.4f}")
    print(f"Recall   : {recall_score(y_test, pred, pos_label='spam', zero_division=0):.4f}")
    print(f"F1-score : {f1_score(y_test, pred, pos_label='spam', zero_division=0):.4f}")
    print("Confusion matrix:")
    print(confusion_matrix(y_test, pred, labels=["ham", "spam"]))

    MODEL_DIR.mkdir(exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    joblib.dump(vectorizer, VECTORIZER_PATH)
    print(f"\nSaved model     -> {MODEL_PATH}")
    print(f"Saved vectorizer-> {VECTORIZER_PATH}")

if __name__ == "__main__":
    main()
