from fastapi import FastAPI
import requests

app = FastAPI()

OLLAMA_URL = "http://127.0.0.1:11434/api/chat"


@app.get("/")
def home():
    return {"status": "Flipper AI Server OK"}


@app.post("/chat")
def chat(data: dict):
    message = data.get("message", "")

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "qwen3.5",
            "messages": [
                {
                    "role": "user",
                    "content": message
                }
            ],
            "stream": False
        },
        timeout=120
    )

    result = response.json()

    return {
        "answer": result["message"]["content"]
    }
