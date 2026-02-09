from yt_dlp import YoutubeDL
from cli_to_api import cli_to_api

class Downloader:
    def __init__(self):
        self.default_options = ["--embed-thumbnail", "--quiet"]

    def downloadAudio(self, links : list, dest="~/Downloads/", playlist=False):
        actual_dest = dest + "%(title)s.%(ext)s"
        options = [
            '-o', actual_dest,
            '-t', 'mp3',
            '--yes-playlist' if playlist else '--no-playlist'
        ] + self.default_options
        self.download(links, options)

    def download(self, links, options):
        api_opt = cli_to_api(options)
        api_opt.update({
            'progress_hooks': [downloading_hook],
            'postprocessor_hooks': [done_hook]
        })
        with YoutubeDL(api_opt) as ytd:
            ytd.download(URL)


def downloading_hook(d):
    if d['status'] == 'downloading':
        print(f"{d['downloaded_bytes'] / d['total_bytes'] * 100.0}%")
    elif d['status'] == 'finished':
        print("FINE DOWNLOAD")
    elif d['status'] == 'error':
        print("ERRORE")

def done_hook(d):
    if d['status'] == 'finished':
        print("TUTTO FATTO!")

URL = ["https://www.youtube.com/watch?v=9ruLQ1Hmhjs"]

dwld = Downloader()
dwld.downloadAudio(URL)
