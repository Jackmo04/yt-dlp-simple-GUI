from yt_dlp import YoutubeDL
from utils.cli_to_api import cli_to_api

class Downloader:

    def __init__(self):
        self.progress_hook = None
        self.postprocessing_hook = None

    def download_audio(self, links : list, dest="~/Downloads/", playlist=False):
        self.download(links, ['-t', 'mp3'], dest, playlist)

    def download_video(self, links : list, dest="~/Downloads/", playlist=False):
        self.download(links, ['-t', 'mp4'], dest, playlist)

    def download(self, links : list, options : list, dest="~/Downloads/", playlist=False):
        actual_dest = dest + "%(title)s.%(ext)s"

        cli_opt = options + [
            '-o', actual_dest,
            '--yes-playlist' if playlist else '--no-playlist',
            "--embed-thumbnail",
            "--quiet"
        ]

        api_opt = cli_to_api(cli_opt)

        api_opt.update({
            'progress_hooks': [self.progress_hook],
            'postprocessor_hooks': [self.postprocessing_hook]
        })

        with YoutubeDL(api_opt) as ytd:
            ytd.download(links)

    def set_progress_hook(self, hook : function):
        self.progress_hook = hook

    def set_postprocessing_hook(self, hook : function):
        self.postprocessing_hook = hook

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

