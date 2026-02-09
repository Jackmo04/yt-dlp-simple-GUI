from downloader import Downloader
from updater import Updater

if __name__ == "__main__":
    URL = ["https://www.youtube.com/watch?v=9ruLQ1Hmhjs"] # TESTING URL

    updater = Updater()
    dl = Downloader()
    # dl.download_audio(URL)
    # print(updater.is_update_available())
    # updater.update_and_restart()