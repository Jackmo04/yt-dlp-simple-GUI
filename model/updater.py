import os
import sys
import subprocess
from yt_dlp import YoutubeDL, update as ytdlp_update

class Updater:
    def __init__(self):
        self.ytdlp_updater = ytdlp_update.Updater(YoutubeDL())

    def is_update_available(self):
        return self.ytdlp_updater.query_update() != None

    def update(self):
        '''
        Should always be called in tandem with restart() to ensure the new version is used immediately after update.
        '''
        if self.is_update_available():
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "yt_dlp"])
                print("Aggiornamento completato. In attesa del riavvio...")
                # Removed automatic restart to allow manual control
                return True

            except subprocess.CalledProcessError as e:
                print(f"Errore durante l'aggiornamento: {e}")
                sys.exit(1)
        else:
            return False

    def restart(self):
        print("Riavvio...")
        os.execv(sys.executable, [sys.executable] + sys.argv)