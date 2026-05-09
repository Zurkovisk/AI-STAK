from fastapi import FastAPI
import requests

app = FastAPI()

OLLAMA_URL = "http://localhost:11434/api/generate"

@app.get("/")
def root():
    return {"status": "online"}

@app.get("/ask")
def ask(q: str):

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3:8b",
            "prompt": q,
            "stream": False
        }
    )

    return response.json()