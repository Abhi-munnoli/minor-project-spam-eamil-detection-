# 🛡️ Spam-email-detection

### AI-Powered Spam Email Detection & Security Dashboard

**SpamShield AI** is a full-stack web application that uses **Machine Learning, Natural Language Processing, Flask and Firebase** to detect whether an email/message is **Spam** or **Not Spam**.

The system combines a **TF-IDF text vectorizer** with a **Logistic Regression classifier** and provides a secure cybersecurity-style dashboard for analyzing messages, viewing prediction history and managing user accounts.

---

## 🚀 Project Preview

> 🔐 **Detect suspicious messages. Protect your inbox. Analyze smarter.**

```text
                 ┌─────────────────────────┐
                 │       User Browser      │
                 │   HTML • CSS • JavaScript│
                 └────────────┬────────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │      Flask Backend      │
                 │    Authentication/API   │
                 └────────────┬────────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │    Text Preprocessing   │
                 │       NLTK / NLP        │
                 └────────────┬────────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │       TF-IDF            │
                 │    Feature Extraction   │
                 └────────────┬────────────┘
                              │
                              ▼
                 ┌─────────────────────────┐
                 │   Logistic Regression  │
                 │     ML Classification   │
                 └────────────┬────────────┘
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
              🔴 SPAM              🟢 NOT SPAM
                    │                   │
                    └─────────┬─────────┘
                              ▼
                 ┌─────────────────────────┐
                 │       Firestore        │
                 │   Prediction History   │
                 └─────────────────────────┘
```

---

# ✨ Key Features

| Feature | Description |
|---|---|
| 🤖 **Spam Detection** | Classifies messages as Spam or Not Spam |
| 🧠 **Machine Learning** | Logistic Regression classification |
| 📊 **TF-IDF** | Converts text into machine-learning features |
| 📝 **NLP Processing** | Text cleaning and preprocessing using NLTK |
| 🔐 **Firebase Authentication** | Secure user registration and login |
| 🛡️ **Protected Sessions** | Flask session-based protected routes |
| ☁️ **Firestore** | Stores prediction history securely |
| 👤 **User Profile** | Displays account and authentication information |
| 👑 **Admin Dashboard** | Admin-level application monitoring |
| 📈 **Model Evaluation** | Accuracy, precision, recall and F1-score |
| 🚦 **Rate Limiting** | Helps protect API endpoints |
| 📱 **Responsive UI** | Works across desktop, tablet and mobile |
| 🌙 **Cybersecurity UI** | Modern dark-themed interface |

---

# 🖥️ Application Screenshots

Add screenshots of your actual application here.

### 🔐 Login

```text
docs/images/login.png
```

![SpamShield AI Login](A:\Spam_Email_Detector\ui_images)

---

### 📊 Dashboard

```text
docs/images/dashboard.png
```

![SpamShield AI Dashboard](docs/images/dashboard.png)

---

### 🔎 Spam Detection

```text
docs/images/analyzer.png
```

![Spam Email Analyzer](docs/images/analyzer.png)

---

### 📜 Prediction History

```text
docs/images/history.png
```

![Prediction History](docs/images/history.png)

---

### 👤 User Profile

```text
docs/images/profile.png
```

![User Profile](docs/images/profile.png)

---

### 👑 Admin Dashboard

```text
docs/images/admin.png
```

![Admin Dashboard](docs/images/admin.png)

> 💡 **Tip:** Create a `docs/images` folder and place your screenshots there using exactly these filenames.

---

# 🧠 Machine Learning Pipeline

SpamShield AI follows this pipeline:

```text
                📩 Input Message
                       │
                       ▼
              🧹 Text Cleaning
                       │
                       ▼
              🔤 Tokenization
                       │
                       ▼
            🚫 Stopword Removal
                       │
                       ▼
               📊 TF-IDF
                       │
                       ▼
          🤖 Logistic Regression
                       │
                       ▼
              📈 Prediction
                 /          \
                /            \
               ▼              ▼
          🔴 SPAM        🟢 NOT SPAM
               │              │
               └──────┬───────┘
                      ▼
              💾 Firestore
```

---

# 🧪 Model Evaluation

The model is evaluated using:

- 🎯 Accuracy
- 🔍 Precision
- 📡 Recall
- ⚖️ F1 Score

Example:

```text
Model Evaluation
────────────────────────────

Accuracy   : XX.XX%
Precision  : XX.XX%
Recall     : XX.XX%
F1 Score   : XX.XX%
```

> Replace the values above with the actual results produced by `train_model.py`.

---

# 🏗️ System Architecture

```text
                         ┌───────────────────┐
                         │      Browser      │
                         │ HTML/CSS/JS       │
                         └─────────┬─────────┘
                                   │
                                   ▼
                    ┌─────────────────────────┐
                    │     Firebase Auth       │
                    │  Login / Registration   │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │      Flask Server       │
                    │ Routes + Sessions + API │
                    └────────────┬────────────┘
                                 │
                 ┌───────────────┼───────────────┐
                 │               │               │
                 ▼               ▼               ▼
          ┌────────────┐  ┌────────────┐  ┌────────────┐
          │    NLTK    │  │   TF-IDF   │  │ Firestore  │
          │ NLP Engine │  │ Vectorizer │  │  Database  │
          └─────┬──────┘  └─────┬──────┘  └────────────┘
                │               │
                └───────┬───────┘
                        ▼
                ┌───────────────┐
                │ ML Classifier │
                │    Logistic   │
                │   Regression  │
                └───────┬───────┘
                        │
                        ▼
                🔴 Spam / 🟢 Safe
```

---

# 🛠️ Technology Stack

### Frontend

```text
HTML5
CSS3
JavaScript
Responsive Design
Font Awesome
```

### Backend

```text
Python
Flask
Flask-Limiter
Jinja2
```

### Machine Learning

```text
Scikit-learn
TF-IDF
Logistic Regression
NLTK
Joblib
```

### Database & Authentication

```text
Firebase Authentication
Cloud Firestore
Firebase Admin SDK
```

---

# 📁 Project Structure

```text
Spam_Email_Detector/
│
├── 📂 dataset/
│   └── spam.csv
│
├── 📂 model/
│   ├── spam_model.pkl
│   └── vectorizer.pkl
│
├── 📂 static/
│   ├── 📂 css/
│   │   └── style.css
│   │
│   ├── 📂 js/
│   │   ├── script.js
│   │   ├── auth.js
│   │   └── dashboard.js
│   │
│   └── 📂 images/
│       └── logo.svg
│
├── 📂 templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── history.html
│   ├── profile.html
│   └── admin.html
│
├── 📂 docs/
│   └── 📂 images/
│       ├── login.png
│       ├── dashboard.png
│       ├── analyzer.png
│       ├── history.png
│       ├── profile.png
│       └── admin.png
│
├── app.py
├── train_model.py
├── requirements.txt
├── firestore.rules
├── .env
├── .gitignore
├── README.md
└── serviceAccountKey.json
```

---

# ⚙️ Installation

## 1️⃣ Clone the Project

```bash
git clone <your-repository-url>
cd Spam_Email_Detector
```

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

Recommended Python version:

```text
Python 3.11+
```

---

# 🔥 Firebase Configuration

Create a Firebase project and enable:

```text
Firebase Authentication
        ↓
Email / Password
        ↓
Cloud Firestore
```

### Firebase Web App

Go to:

```text
Firebase Console
→ Project Settings
→ Your Apps
→ Web App
```

Copy the Firebase configuration values into `.env`.

### Service Account

Go to:

```text
Firebase Console
→ Project Settings
→ Service Accounts
→ Generate New Private Key
```

Save the downloaded file as:

```text
serviceAccountKey.json
```

Place it in:

```text
Spam_Email_Detector/
└── serviceAccountKey.json
```

---

# 🔐 Environment Variables

Create:

```text
.env
```

Example:

```env
FLASK_SECRET_KEY=your-long-random-secret

FIREBASE_WEB_API_KEY=your-api-key
FIREBASE_AUTH_DOMAIN=your-project.firebaseapp.com
FIREBASE_PROJECT_ID=your-project-id
FIREBASE_STORAGE_BUCKET=your-project.appspot.com
FIREBASE_MESSAGING_SENDER_ID=your-sender-id
FIREBASE_APP_ID=your-app-id

ADMIN_EMAILS=your-admin-email@example.com
```

⚠️ Never upload `.env` or `serviceAccountKey.json` to GitHub.

---

# 📊 Dataset

The project expects a CSV dataset containing:

```text
label,message
```

Example:

```text
label,message
ham,"Can you send me the project report?"
spam,"Congratulations! You have won a prize!"
```

The training script also recognizes common alternatives such as:

```text
category
class
target
text
email
body
```

For meaningful real-world evaluation, use a **larger, representative and properly licensed dataset**.

---

# 🤖 Train the Model

Run:

```bash
python train_model.py
```

The training process generates:

```text
model/
├── spam_model.pkl
└── vectorizer.pkl
```

---

# 🚀 Run the Application

Start Flask:

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000
```

---

# 🔐 Authentication Flow

```text
Register
   ↓
Firebase Authentication
   ↓
Firebase ID Token
   ↓
Flask Verification
   ↓
Protected Session
   ↓
Dashboard
```

Users can:

```text
Create Account
      ↓
Login
      ↓
Analyze Messages
      ↓
View Results
      ↓
View Prediction History
      ↓
View Profile
```

---

# 👑 Admin System

An administrator can be configured through:

```env
ADMIN_EMAILS=admin@example.com
```

The admin account can access:

```text
Admin Dashboard
      │
      ├── 👥 Users
      ├── 📊 Predictions
      ├── 🔴 Spam Statistics
      └── 📈 System Overview
```

For production systems, Firebase **custom claims** are recommended for stronger admin authorization.

---

# ☁️ Firestore

Prediction records are stored in Firestore.

Example:

```text
predictions/
   │
   ├── prediction_id
   │     ├── uid
   │     ├── message
   │     ├── prediction
   │     ├── confidence
   │     └── created_at
```

This allows users to view their previous spam detection results.

---

# 🛡️ Security

SpamShield AI includes several security mechanisms:

### 🔐 Authentication

Firebase Authentication protects user accounts.

### 🛡️ Protected Sessions

Flask sessions protect authenticated application routes.

### 🚦 Rate Limiting

API endpoints are rate-limited to reduce abuse.

### 🧹 Input Validation

User input is validated before processing.

### ☁️ Firestore Rules

Firestore rules restrict direct client access.

### 🔑 Secret Management

Sensitive credentials are stored outside frontend code.

---

# 🚨 Important Security Rules

Never commit:

```text
.env
serviceAccountKey.json
```

Add them to:

```text
.gitignore
```

Example:

```gitignore
.env
serviceAccountKey.json
venv/
__pycache__/
*.pyc
```

---

# 🧪 Testing the Detector

Try different types of messages.

### 🟢 Normal

```text
Can you send me the project report after class?
```

Expected:

```text
🟢 NOT SPAM
```

### 🔴 Suspicious

```text
You have been selected for an exclusive reward. Verify your information immediately.
```

Expected:

```text
🔴 SPAM
```

Test different categories such as:

```text
📧 Personal messages
🎓 College messages
🛒 Shopping notifications
🏦 Financial messages
🎁 Fake rewards
💰 Investment scams
🔐 Phishing attempts
📱 Promotional messages
```

---

# 🧰 Troubleshooting

## Model Not Found

Run:

```bash
python train_model.py
```

Make sure these files exist:

```text
model/spam_model.pkl
model/vectorizer.pkl
```

---

## Firebase Configuration Error

Check:

```text
.env
```

Make sure all Firebase Web App configuration values are present.

---

## Firestore Error

Check:

```text
serviceAccountKey.json
```

Make sure it belongs to the correct Firebase project.

---

## Admin Page Not Available

Check:

```env
ADMIN_EMAILS=your-email@example.com
```

Then:

```text
Logout
↓
Login again
```

---

## NLTK Resource Error

Run:

```python
import nltk

nltk.download("stopwords")
```

---

# 📈 Future Improvements

Planned improvements include:

```text
🔹 Larger training dataset
🔹 Advanced NLP models
🔹 BERT-based classification
🔹 Email attachment analysis
🔹 URL phishing detection
🔹 Real-time email scanning
🔹 Explainable AI predictions
🔹 Advanced admin analytics
🔹 User activity monitoring
🔹 Email API integration
🔹 Multi-language spam detection
🔹 Docker deployment
```

---

# 🎯 Project Objectives

The main objectives of SpamShield AI are:

- Detect spam messages automatically.
- Apply machine learning to text classification.
- Provide a secure web-based detection platform.
- Store prediction history using Firestore.
- Implement Firebase-based authentication.
- Provide administrators with monitoring capabilities.
- Demonstrate the practical use of NLP and machine learning.

---

# 🏆 Project Highlights

```text
                 🛡️ SPAMSHIELD AI

          ┌─────────────────────────┐
          │       AI Detection      │
          └────────────┬────────────┘
                       │
       ┌───────────────┼───────────────┐
       ▼               ▼               ▼
   🤖 Machine       🔐 Secure        ☁️ Firebase
    Learning       Authentication     Firestore
       │               │               │
       └───────────────┼───────────────┘
                       ▼
                📊 Smart Dashboard
```

---

# 📚 Technologies Used

```text
Python
Flask
Scikit-learn
NLTK
Pandas
Joblib
Firebase Authentication
Cloud Firestore
HTML5
CSS3
JavaScript
```

---

# ⚠️ Disclaimer

SpamShield AI is an educational and demonstration project.

The machine-learning classifier should **not be treated as a definitive security control**. Real-world email security should also use established anti-spam, phishing detection, malware scanning and authentication mechanisms.

---

# 👨‍💻 Developer

### **SpamShield AI**

Built as a Machine Learning + Full-Stack Web Application using:

```text
🐍 Python
⚡ Flask
🧠 Machine Learning
🔤 NLP
🔥 Firebase
☁️ Firestore
🎨 HTML / CSS / JavaScript
```

---

# ⭐ Support the Project

If you find this project useful:

```text
⭐ Star the repository
🍴 Fork the repository
🐛 Report issues
💡 Suggest improvements
📢 Share the project
```

---

## 🛡️ SpamShield AI

### **Detect • Analyze • Protect**

> **Turning Machine Learning into smarter email security.**
