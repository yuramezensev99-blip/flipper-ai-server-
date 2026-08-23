import requests
import json
import sys

with open("config.json") as f:
    cfg = json.load(f)

URL = f"http://{cfg['host']}:{cfg['port']}"

def status():
    try:
        r = requests.get(URL + "/status", timeout=5)
        print(r.json())
    except Exception as e:
        print("Ошибка:", e)

if len(sys.argv) > 1:
    if sys.argv[1] == "status":
        status()
