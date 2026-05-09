from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import requests
import os
import time

OLLAMA_URL = "http://localhost:11434/api/generate"

WATCH_DIR = "../workspace"

class Handler(FileSystemEventHandler):
    def on_modified(self, event):

        if event.is_directory:
            return

        if not event.src_path.endswith(".py"):
            return

        print(f"[AI] Refatorando {event.src_path}")

        with open(event.src_path, "r") as f:
            code = f.read()

        prompt = f"""
Refatore este código mantendo funcionalidade.
Melhore:
- legibilidade
- performance
- boas práticas

Código:
{code}
"""

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "deepseek-coder:6.7b",
                "prompt": prompt,
                "stream": False
            }
        )

        output = response.json()["response"]

        with open(event.src_path, "w") as f:
            f.write(output)

observer = Observer()
observer.schedule(Handler(), WATCH_DIR, recursive=True)

observer.start()

print("👀 Watcher iniciado")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()