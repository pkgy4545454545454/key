import os
from flask import Flask, request

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
