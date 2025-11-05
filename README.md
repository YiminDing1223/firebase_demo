# Firebase + FastAPI Demo 🚀

This project demonstrates a simple **Firebase Authentication + Firestore + FastAPI** integration.
Users can log in via Firebase, and the app retrieves personalized text from Firestore using a backend API.

---

## 🌐 Project Structure

```
firebase_demo/
├── backend/
│   ├── main.py
│   └── practice-e2b0c-firebase-adminsdk-fbsvc-6ed393b5fe.json
├── frontend/
│   ├── index.html
│   └── main.js
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Backend (FastAPI + Firestore)
```bash
cd backend
pip install fastapi uvicorn google-cloud-firestore python-dotenv
uvicorn main:app --host 0.0.0.0 --port 8080
```

### 2️⃣ Frontend (Firebase Auth)
```bash
cd frontend
python3 -m http.server 5500
```

Then open [http://127.0.0.1:5500/index.html](http://127.0.0.1:5500/index.html)

---

## 🔐 Authentication
Login with your Firebase Authentication credentials (email + password).

Example test user:
```
Email: yiminding61@gmail.com
Password: 123456
```

---

## ☁️ Firestore Data Structure

Collection: `user_lines`

| Document ID (UID)              | Field | Type   | Example Value |
|-------------------------------|--------|--------|----------------|
| zn8ujnUAjTZzuq6yLj5C5iSF0Lz1 | text   | string | "Straykids everywhere all around the world!" |

---

## 💡 Features
- Firebase Authentication (Email/Password)
- Firestore document retrieval
- FastAPI backend with CORS support
- Simple frontend hosted locally

---

## 👩🏻‍💻 Author
**Yimin Ding**  
