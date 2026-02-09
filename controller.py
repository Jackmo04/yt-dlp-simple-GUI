from downloader import Downloader
from updater import Updater

class Controller:
    def __init__(self, gui):
        self.gui = gui
        self.updater = Updater()
        # print(updater.is_update_available())
        # updater.update_and_restart()

        self.dl = Downloader()
        self.dl.set_progress_hook(progress_hook)
        self.dl.set_postprocessing_hook(postprocessing_hook)

def progress_hook(d):
    if d['status'] == 'downloading':
        completion = int(d['downloaded_bytes'] / d['total_bytes'] * 100)
        print(f"{completion}%", end=' > ')
    elif d['status'] == 'finished':
        print("FINE DOWNLOAD")
    elif d['status'] == 'error':
        print("ERRORE")

def postprocessing_hook(d):
    if d['status'] == 'finished':
        print(d['postprocessor'], "-- FINITO!")

# URL = ["https://www.youtube.com/watch?v=9ruLQ1Hmhjs"] # TESTING URL
# dl.download_audio(URL)