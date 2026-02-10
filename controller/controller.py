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
        self.current = 0

        # URL = ["https://www.youtube.com/watch?v=9ruLQ1Hmhjs"] # TESTING URL
        # self.dl.download_audio(URL)

    def new_download(self, todo):
        self.num_todo = todo
        self.current = 1
        self.view.update_single_progress(self.current, self.num_todo, 0)
        self.view.update_total_progress(0)

    def download_audio(self, links : list, playlist : bool):
        self.new_download(len(links))
        self.dl.download_audio(links, playlist)

    def download_video(self, links : list, playlist : bool):
        self.new_download(len(links))
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
            self.view.update_single_progress(self.current, self.num_todo, completion)
        elif d['status'] == 'finished':
            print("FINE DOWNLOAD")
        elif d['status'] == 'error':
            print("ERRORE")

    def postprocessing_hook(self, d):
        if d['status'] == 'finished':
            if d['postprocessor'] == 'MoveFiles':
                totale_completion = int(self.current / self.num_todo * 100)
                self.view.update_total_progress(totale_completion)
                if self.current < self.num_todo:
                    self.current += 1
                

