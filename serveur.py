from flask import Flask, request, abort
import requests
import os 
from dotenv import load_dotenv
from pathlib import Path
from httpcore import URL

ROOT_DIR = Path(__file__).parent

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "log.txt")


app = Flask(__name__)

@app.post("/log")
def log():
    data = request.get_json(silent=True)
    key = data.get("content") if data else None

    if key:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(key + "\n")
        return "reçue", 200

    return "Erreur : contenu manquant", 400

app.run(host="0.0.0.0", port=5000)
