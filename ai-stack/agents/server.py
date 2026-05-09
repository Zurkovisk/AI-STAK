from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/status")
def status():
    return {"status": "running"}

@app.get("/ai")
def ai(query: str):
    result = subprocess.run(
        ["ollama", "run", "llama3:8b"],
        input=query,
        text=True,
        capture_output=True
    )
    return {"response": result.stdout}