from model.downloader import Downloader
from model.updater import Updater

class Controller:
    def __init__(self, view=None):
        self.view = view
        
        self.updater = Updater()
        self.update_available = self.updater.is_update_available()

        self.dl = Downloader()
        self.dl.set_progress_hook(self.progress_hook)
        self.dl.set_postprocessing_hook(self.postprocessing_hook)

        self.num_todo = 0
        self.num_done = 0

        # URL = ["https://www.youtube.com/watch?v=9ruLQ1Hmhjs"] # TESTING URL
        # self.dl.download_audio(URL)

    def download_audio(self, links : list, playlist : bool):
        self.dl.download_audio(links, playlist)

    def download_video(self, links : list, playlist : bool):
        self.dl.download_video(links, playlist)

    def is_update_available(self):
        return self.update_available
    
    def update(self):
        return self.updater.update()

    def restart(self):
        self.updater.restart()

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            completion = int(d['downloaded_bytes'] / d['total_bytes'] * 100)
            self.view.update_progress(completion)
        elif d['status'] == 'finished':
            print("FINE DOWNLOAD")
        elif d['status'] == 'error':
            print("ERRORE")

    def postprocessing_hook(self, d):
        if d['status'] == 'finished':
            print(d['postprocessor'], "-- FINITO!")

