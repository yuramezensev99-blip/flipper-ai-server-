from fastapi import FastAPI, UploadFile, File
import requests

app = FastAPI(title="Flipper AI Core")

OLLAMA_URL = "вставьте ip адрес ollama server /api/chat"
OLLAMA_TAGS = "вставьте ip адрес ollama server/api/tags"

MODEL = "название модели "

@app.get("/")
def home():
    return {
        "status": "Flipper AI Core online"
    }

@app.get("/test")
def test():
    return {
        "api": "ok"
    }

@app.get("/models")
def models():
    r = requests.get(OLLAMA_TAGS)

    return r.json()

@app.post("/chat")
def chat(data: dict):

    message = data.get("message", "")

    if not message:
        return {
            "error": "empty message"
        }

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "messages": [
                {
                    "role": "system",
                    "content":
                    "Ты локальный AI ассистент Flipper. Отвечай на русском кратко и по делу."
                },
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

@app.post("/vision")
def vision():
    return {
        "status": "vision module placeholder"
    }

@app.post("/flipper")
def flipper():
    return {
        "status": "flipper module placeholder"
    }
