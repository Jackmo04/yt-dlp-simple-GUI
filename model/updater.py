import os
import sys
import subprocess
from yt_dlp import YoutubeDL, update as ytdlp_update

class Updater:
    def __init__(self):
        self.ytdlp_updater = ytdlp_update.Updater(YoutubeDL())

    def is_update_available(self):
        return self.ytdlp_updater.query_update() != None

    def update_and_restart(self):
        if self.is_update_available():
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "yt_dlp"])
                print("Aggiornamento completato. Riavvio...")
                os.execv(sys.executable, [sys.executable] + sys.argv)

            except subprocess.CalledProcessError as e:
                print(f"Errore durante l'aggiornamento: {e}")
                sys.exit(1)
        else:
            print("No update available")