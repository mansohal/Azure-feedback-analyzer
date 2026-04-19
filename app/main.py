from fastapi import FastAPI
import uuid
import os

app = FastAPI()

DATA_FOLDER = "../data"
os.makedirs(DATA_FOLDER, exist_ok=True)

@app.get("/")
def home():
    return {"message": "API running"}

@app.post("/upload")
def upload(text: str):
    file_id = str(uuid.uuid4())
    filepath = os.path.join(DATA_FOLDER, file_id + ".txt")
    
    with open(filepath, "w") as f:
        f.write(text)
    
    return {"id": file_id}