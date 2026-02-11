from model.downloader import Downloader
from model.updater import Updater
import sys

class Controller:
    def __init__(self, view=None):
        self.view = view

        # Auto updates for compiled versions aren't supported yet
        if not getattr(sys, 'frozen', False):
            self.updater = Updater()
            self.update_available = self.updater.is_update_available()
        else:
            self.update_available = False

        self.dl = Downloader()
        self.dl.set_progress_hook(self.progress_hook)
        self.dl.set_postprocessing_hook(self.postprocessing_hook)

        self.num_todo = 0
        self.current = 0

    def new_download(self, handler, links : list, playlist : bool):
        self.num_todo = len(links)
        self.current = 1
        self.view.update_single_progress(self.current, self.num_todo, 0)
        self.view.update_total_progress(0)
        try:
            handler(links, playlist)
        except Exception as e:
            self.view.display_error("Errore", f"Si è verificato un errore durante il download:\n{str(e).split('] ')[-1]}")
            self.current = 0
            self.num_todo = 0
            self.view.update_single_progress(self.current, self.num_todo, 0)
            self.view.update_total_progress(0)

    def download_audio(self, links : list, playlist : bool):
        self.new_download(self.dl.download_audio, links, playlist)

    def download_video(self, links : list, playlist : bool):
        self.new_download(self.dl.download_video, links, playlist)

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
            print(f"Completato download {self.current} di {self.num_todo}")
        elif d['status'] == 'error':
            self.view.display_error("Errore", "Si è verificato un errore durante il download.")

    def postprocessing_hook(self, d):
        if d['status'] == 'finished':
            if d['postprocessor'] == 'MoveFiles':
                totale_completion = int(self.current / self.num_todo * 100)
                self.view.update_total_progress(totale_completion)
                if self.current < self.num_todo:
                    self.current += 1
                else:
                    self.view.display_success("Download completato", "Download completato con successo!")
                

