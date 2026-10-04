# 🛡️ SpamShield AI

### AI-Powered Spam Email Detection & Security Dashboard

SpamShield AI is a full-stack Spam Email Detection web application using **Python, Flask, scikit-learn, NLTK, Firebase Authentication and Cloud Firestore**.

> 🔐 **Detect • Analyze • Protect**

---

## 🚀 Project Overview

SpamShield AI uses **Machine Learning and Natural Language Processing** to classify messages as **Spam** or **Not Spam**.

### ✨ Features

- 🤖 Spam / Not Spam Classification
- 🧠 Logistic Regression Machine Learning
- 📊 TF-IDF Text Feature Extraction
- 📝 NLTK Text Preprocessing
- 🔐 Firebase Authentication
- 🛡️ Protected Flask Sessions
- ☁️ Firestore Prediction History
- 👤 User Profile
- 👑 Admin Dashboard
- 📈 Accuracy, Precision, Recall and F1 Evaluation
- 🚦 Rate Limiting
- 📱 Responsive UI
- 🌙 Modern Cybersecurity-Style Interface

---

# 🖥️ Application Screenshots

## 🏠 1. Home Page

**File:** `A:\Spam_Email_Detector\ui_images\1.home.png`

![SpamShield AI Home Page](file:///A:/Spam_Email_Detector/ui_images/1.home.png)

---

## 👤 2. Account Creation

**File:** `A:\Spam_Email_Detector\ui_images\2. account create.png`

![SpamShield AI Account Creation](file:///A:/Spam_Email_Detector/ui_images/2.%20account%20create.png)

---

## 🔐 3. Login Page

**File:** `A:\Spam_Email_Detector\ui_images\3.login.png`

![SpamShield AI Login](file:///A:/Spam_Email_Detector/ui_images/3.login.png)

---

## 📊 4. Dashboard

**File:** `A:\Spam_Email_Detector\ui_images\4.dashboard.png`

![SpamShield AI Dashboard](file:///A:/Spam_Email_Detector/ui_images/4.dashboard.png)

---

## 🔎 5. Analyze Message

**File:** `A:\Spam_Email_Detector\ui_images\5.Analyze Message.png`

![SpamShield AI Analyze Message](file:///A:/Spam_Email_Detector/ui_images/5.Analyze%20Message.png)

---

## 📜 6. History Page

**File:** `A:\Spam_Email_Detector\ui_images\6.History page 1.png`

![SpamShield AI History](file:///A:/Spam_Email_Detector/ui_images/6.History%20page%201.png)

---

## 👤 7. Profile Edit

**File:** `A:\Spam_Email_Detector\ui_images\8. profile edit.png`

![SpamShield AI Profile](file:///A:/Spam_Email_Detector/ui_images/8.%20profile%20edit.png)

---

## 🔥 8. Firebase Datastore

**File:** `A:\Spam_Email_Detector\ui_images\9.firebase datastore.png`

![SpamShield AI Firebase Datastore](file:///A:/Spam_Email_Detector/ui_images/9.firebase%20datastore.png)

---

# 🧠 Machine Learning Pipeline

```text
📩 Input Message
       ↓
🧹 Text Preprocessing
       ↓
🔤 Tokenization
       ↓
🚫 Stopword Removal
       ↓
📊 TF-IDF Vectorization
       ↓
🤖 Logistic Regression
       ↓
📈 Prediction
       ↓
┌───────────────┬───────────────┐
▼               ▼
🔴 SPAM         🟢 NOT SPAM
└───────────────┴───────────────┘
       ↓
☁️ Firestore Prediction History

# 🏗️ System Architecture

```text
                         ┌──────────────────────┐
                         │       USER           │
                         │   Web Browser        │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   HTML / CSS / JS    │
                         │    Frontend UI       │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Firebase             │
                         │ Authentication       │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Flask Backend        │
                         │ API + Sessions      │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ NLP Preprocessing    │
                         │ NLTK                │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ TF-IDF Vectorizer   │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │ Logistic Regression │
                         │ ML Classifier       │
                         └──────────┬───────────┘
                                    │
                           ┌────────┴────────┐
                           ▼                 ▼
                     🔴 SPAM          🟢 NOT SPAM
                           │                 │
                           └────────┬────────┘
                                    ▼
                         ┌──────────────────────┐
                         │ Cloud Firestore     │
                         │ Prediction History  │
                         └──────────────────────┘
```

---

# 🛠️ Technology Stack

## 🎨 Frontend

```text
HTML5
CSS3
JavaScript
Jinja2 Templates
Font Awesome
Responsive Design
```

## ⚡ Backend

```text
Python
Flask
Flask-Limiter
Jinja2
```

## 🧠 Machine Learning

```text
Scikit-learn
TF-IDF
Logistic Regression
NLTK
Pandas
Joblib
```

## 🔥 Firebase

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
├── 📂 ui_images/
│   ├── 1.home.png
│   ├── 2. account create.png
│   ├── 3.login.png
│   ├── 4.dashboard.png
│   ├── 5.Analyze Message.png
│   ├── 6.History page 1.png
│   ├── 8. profile edit.png
│   └── 9.firebase datastore.png
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

---

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

Recommended:

```text
Python 3.11+
```

---

# 🔥 Firebase Setup

Create a Firebase project and enable:

```text
Firebase Authentication
        ↓
Email / Password
        ↓
Cloud Firestore
```

### Firebase Web Application

Go to:

```text
Firebase Console
→ Project Settings
→ Your Apps
→ Web App
```

Copy the Firebase Web App configuration into `.env`.

### Service Account

Go to:

```text
Firebase Console
→ Project Settings
→ Service Accounts
→ Generate New Private Key
```

Save the downloaded JSON file as:

```text
serviceAccountKey.json
```

Place it in the project root:

```text
Spam_Email_Detector/
└── serviceAccountKey.json
```

---

# 🔐 Environment Variables

Create a `.env` file:

```env
FLASK_SECRET_KEY=generate-a-long-random-secret

FIREBASE_WEB_API_KEY=your-api-key
FIREBASE_AUTH_DOMAIN=your-project.firebaseapp.com
FIREBASE_PROJECT_ID=your-project-id
FIREBASE_STORAGE_BUCKET=your-project.appspot.com
FIREBASE_MESSAGING_SENDER_ID=your-sender-id
FIREBASE_APP_ID=your-app-id

ADMIN_EMAILS=your-admin-email@example.com
```

⚠️ **Never upload `.env` or `serviceAccountKey.json` to GitHub.**

---

# 📊 Dataset

The project expects:

```text
label,message
```

Example:

```text
label,message
ham,"Can you send me the project report?"
spam,"Congratulations! You have won a prize!"
```

The trainer also recognizes common alternatives such as:

```text
category
class
target
text
email
body
```

For meaningful real-world evaluation, use a larger, representative and properly licensed dataset.

---

# 🤖 Train the Model

Run:

```bash
python train_model.py
```

The training process creates:

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

Open:

```text
http://127.0.0.1:5000
```

---

# 🔐 Authentication Flow

```text
              👤 User
                 │
                 ▼
            📝 Register
                 │
                 ▼
       🔥 Firebase Authentication
                 │
                 ▼
          🔑 Firebase ID Token
                 │
                 ▼
          ⚡ Flask Verification
                 │
                 ▼
          🛡️ Protected Session
                 │
                 ▼
             📊 Dashboard
```

---

# 👑 Admin System

An administrator can be configured using:

```env
ADMIN_EMAILS=admin@example.com
```

Admin functionality can include:

```text
👥 User Management
📊 Prediction Statistics
🔴 Spam Statistics
📈 System Monitoring
☁️ Firestore Data
```

For production applications, Firebase **custom claims** are recommended for stronger admin authorization.

---

# ☁️ Firestore Database

Prediction information is stored in Cloud Firestore.

Example structure:

```text
Firestore
│
├── users/
│   └── user_id
│       ├── name
│       ├── email
│       ├── role
│       └── created_at
│
└── predictions/
    └── prediction_id
        ├── uid
        ├── message
        ├── prediction
        ├── confidence
        └── created_at
```

---

# 🛡️ Security

SpamShield AI includes multiple security features:

### 🔐 Firebase Authentication

Provides secure user registration and login.

### 🛡️ Protected Flask Sessions

Authenticated routes are protected using server-side sessions.

### 🚦 Rate Limiting

Helps reduce excessive API requests.

### 🧹 Input Validation

User-provided messages are validated before processing.

### ☁️ Firestore

Stores prediction information securely.

### 🔑 Secret Management

Sensitive Firebase service credentials are kept outside frontend JavaScript.

---

# 🚨 Security Rules

Never commit:

```text
.env
serviceAccountKey.json
```

Add them to `.gitignore`:

```gitignore
.env
serviceAccountKey.json
venv/
__pycache__/
*.pyc
```

---

# 🧪 Testing

Test the system with different message categories.

### 🟢 Normal Message

```text
Can you send me the project report after class?
```

Expected:

```text
🟢 NOT SPAM
```

### 🔴 Suspicious Message

```text
You have been selected for an exclusive reward. Verify your information immediately.
```

Expected:

```text
🔴 SPAM
```

Test categories such as:

```text
📧 Personal Messages
🎓 College Messages
🛒 Shopping Notifications
🏦 Financial Messages
🎁 Fake Rewards
💰 Investment Scams
🔐 Phishing Attempts
📱 Promotional Messages
```

---

# 📈 Model Evaluation

The machine learning model can be evaluated using:

```text
🎯 Accuracy
🔍 Precision
📡 Recall
⚖️ F1 Score
```

Example output:

```text
Model Evaluation
────────────────────────

Accuracy   : XX.XX%
Precision  : XX.XX%
Recall     : XX.XX%
F1 Score   : XX.XX%
```

Replace the values with the actual results generated by:

```bash
python train_model.py
```

---

# 🧰 Troubleshooting

## Model Not Found

Run:

```bash
python train_model.py
```

Verify:

```text
model/spam_model.pkl
model/vectorizer.pkl
```

---

## Firebase Configuration Error

Check `.env` and verify that all Firebase Web App configuration values are present.

---

## Firestore Error

Verify:

```text
serviceAccountKey.json
```

Make sure it belongs to the same Firebase project.

---

## Admin Page Unavailable

Verify:

```env
ADMIN_EMAILS=your-admin-email@example.com
```

Then:

```text
Logout
   ↓
Login Again
   ↓
Admin Dashboard
```

---

## NLTK Resource Error

Run:

```python
import nltk
nltk.download("stopwords")
```

---

# 🎯 Project Objectives

The main objectives of SpamShield AI are:

- 🤖 Automatically detect spam messages.
- 🧠 Apply machine learning to text classification.
- 🔤 Use NLP for text processing.
- 🔐 Provide secure user authentication.
- ☁️ Store prediction history using Firestore.
- 📊 Provide a modern cybersecurity dashboard.
- 👑 Provide administrator monitoring capabilities.
- 🛡️ Demonstrate practical application of machine learning and web technologies.

---

# 🚀 Future Improvements

Possible future enhancements:

```text
🔹 Larger training dataset
🔹 Advanced NLP models
🔹 BERT-based classification
🔹 URL phishing detection
🔹 Email attachment analysis
🔹 Real-time email scanning
🔹 Explainable AI predictions
🔹 Advanced admin analytics
🔹 User activity monitoring
🔹 Email API integration
🔹 Multi-language spam detection
🔹 Docker deployment
🔹 Cloud deployment
```

---

# 🏆 Project Highlights

```text
              🛡️ SPAMSHIELD AI

        AI-Powered Spam Detection
                  │
        ┌─────────┼─────────┐
        │         │         │
        ▼         ▼         ▼
       🤖        🔐        ☁️
   Machine     Secure    Firebase
   Learning    Auth      Firestore
        │         │         │
        └─────────┼─────────┘
                  │
                  ▼
           📊 Smart Dashboard
                  │
                  ▼
        🔴 Spam / 🟢 Not Spam
```

---

# 📚 Technologies Used

```text
🐍 Python
⚡ Flask
🧠 Scikit-learn
🔤 NLTK
📊 Pandas
💾 Joblib
🔥 Firebase Authentication
☁️ Cloud Firestore
🌐 HTML5
🎨 CSS3
⚙️ JavaScript
```

---

# ⚠️ Disclaimer

SpamShield AI is an educational and demonstration project.

The machine-learning classifier should **not be treated as a definitive security control**.

Real-world email security should also use established:

- Anti-spam systems
- Phishing detection
- Malware scanning
- Email authentication
- Domain reputation systems
- Security monitoring

---

# 👨‍💻 Developer

## 🛡️ SpamShield AI

Built using:

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

<div align="center">

## 🛡️ SpamShield AI

### **Detect • Analyze • Protect**

**Turning Machine Learning into smarter email security.**

</div>
