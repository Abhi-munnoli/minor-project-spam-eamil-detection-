# 🛡️ SpamShield AI

SpamShield AI is a full-stack Spam Email Detection web application using Python, Flask, scikit-learn, NLTK, Firebase Authentication and Firestore.

## Features

- Spam / Not Spam classification
- TF-IDF text features
- Logistic Regression classifier
- Accuracy, precision, recall and F1 evaluation
- Firebase Authentication
- Protected Flask sessions
- Firestore prediction history
- User profile
- Admin dashboard
- Responsive cybersecurity-style UI
- Rate limiting and input validation

## 1. Requirements

Python 3.11+ is recommended.

## 2. Setup

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install:

```bash
pip install -r requirements.txt
```

## 3. Firebase setup

1. Create a Firebase project.
2. Enable Authentication → Sign-in method → Email/Password.
3. Create a Firestore database.
4. In Project Settings → Your apps, create a Web App and copy the web configuration into `.env`.
5. In Project Settings → Service Accounts, generate a private key.
6. Save that private key as `serviceAccountKey.json` in the project root.
7. Never commit that file to Git.
8. Set `ADMIN_EMAILS` in `.env` to the email(s) that should receive the application admin role.

Example `.env`:

```env
FLASK_SECRET_KEY=generate-a-long-random-secret
FIREBASE_WEB_API_KEY=...
FIREBASE_AUTH_DOMAIN=...
FIREBASE_PROJECT_ID=...
FIREBASE_STORAGE_BUCKET=...
FIREBASE_MESSAGING_SENDER_ID=...
FIREBASE_APP_ID=...
ADMIN_EMAILS=your-admin-email@example.com
```

## 4. Dataset

The included `dataset/spam.csv` is a small demo dataset for testing the complete pipeline. For meaningful model evaluation, replace it with a larger, representative and properly licensed spam/ham dataset.

Expected columns:

```text
label,message
```

The trainer also recognizes common alternatives such as category/class/target and text/email/body.

## 5. Train the model

```bash
python train_model.py
```

This creates:

```text
model/spam_model.pkl
model/vectorizer.pkl
```

## 6. Run

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## 7. Admin

Register using an email listed in `ADMIN_EMAILS`. The first authenticated session for that account is stored with the admin role.

For stronger production deployments, use Firebase custom claims for admin authorization rather than an environment email allowlist.

## 8. Firestore rules

Deploy the included rules with Firebase CLI:

```bash
firebase deploy --only firestore:rules
```

The Flask server uses Firebase Admin SDK, so its server-side writes are not blocked by client Firestore rules. The rules still protect direct client access.

## 9. Security notes

- Never expose `serviceAccountKey.json`.
- Never place service-account credentials in frontend JavaScript.
- Use HTTPS in production.
- Set a strong `FLASK_SECRET_KEY`.
- Restrict Firestore access.
- Replace the demo dataset before evaluating real-world performance.
- Do not treat the model as a definitive security control; combine it with normal email security controls for real systems.

## 10. Architecture

```text
Browser
  ↓
Flask templates + JavaScript
  ↓
Firebase Authentication
  ↓
Flask session / protected API
  ↓
Text preprocessing → TF-IDF → Logistic Regression
  ↓
Spam / Not Spam + confidence
  ↓
Firestore prediction history
```

## 11. Troubleshooting

### Model not found
Run:

```bash
python train_model.py
```

### Firebase authentication configuration missing
Check `.env` and make sure the Firebase Web App configuration is present.

### Firestore unavailable
Check that `serviceAccountKey.json` exists and belongs to the same Firebase project.

### Admin page unavailable
Make sure the signed-in email is listed in `ADMIN_EMAILS`, then log out and sign in again.

### NLTK resource error
Run:

```python
import nltk
nltk.download("stopwords")
```
