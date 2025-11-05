import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from google.cloud import firestore

import os
from pathlib import Path


key_path = Path.home() / "firebase_keys_practice-e2b0c.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(key_path)

db = firestore.Client()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health_check():
    return {"status": "ok", "message": "FastAPI backend is running."}

@app.get("/line")
def get_line(user_id: str):
    """
    Example: GET /line?user_id=some_uid

    1) Retrieve the document from the Firestore collection 'user_lines' 
   that matches the given user_id.
    2) Return the value of its 'text' field as the response.
    """


    doc_ref = db.collection("user_lines").document(user_id)
    doc = doc_ref.get()

    if not doc.exists:
        raise HTTPException(status_code=404, detail="No line found for this user.")

    data = doc.to_dict()
    text = data.get("text", "")

    return {"text": text}
