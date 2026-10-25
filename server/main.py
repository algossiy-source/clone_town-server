
from fastapi import FastAPI

app = FastAPI(title="Clone Town Server")

@app.get("/")
def home():
    return {"status": "online", "service": "Clone Town Server"}

@app.get("/health")
def health():
    return {"status": "ok"}
