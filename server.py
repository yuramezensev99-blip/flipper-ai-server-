import requests
import json

with open("config.json") as f:
    config = json.load(f)

SERVER = config["server"]

def chat(message):
    try:
        response = requests.post(
            SERVER + "/chat",
            json={
                "message": message
            },
            timeout=30
        )

        response.raise_for_status()

        data = response.json()
        return data

    except Exception as e:
        return {
            "error": str(e)
        }

print("Flipper Client запущен")
print("Введите exit для выхода\n")

while True:
    msg = input("Ты: ")

    if msg.lower() == "exit":
        break

    result = chat(msg)

    print("Ответ:", result)
