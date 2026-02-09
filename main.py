from downloader import Downloader
from updater import Updater

def progress_hook(d):
    if d['status'] == 'downloading':
        print(f"{d['downloaded_bytes'] / d['total_bytes'] * 100.0}%")
    elif d['status'] == 'finished':
        print("FINE DOWNLOAD")
    elif d['status'] == 'error':
        print("ERRORE")

def postprocessing_hook(d):
    if d['status'] == 'finished':
        print(d['postprocessor'], "-- FINITO!")

if __name__ == "__main__":
    URL = ["https://www.youtube.com/watch?v=9ruLQ1Hmhjs"] # TESTING URL

    updater = Updater()
    dl = Downloader()

    dl.set_progress_hook(progress_hook)
    dl.set_postprocessing_hook(postprocessing_hook)

    dl.download_audio(URL)
    # print(updater.is_update_available())
    # updater.update_and_restart()