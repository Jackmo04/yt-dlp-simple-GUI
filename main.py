from downloader import Downloader

if __name__ == "__main__":
    URL = ["https://www.youtube.com/watch?v=9ruLQ1Hmhjs"] # TESTING URL

    dl = Downloader()
    # dl.download_audio(URL)
    print(dl.check_updates())