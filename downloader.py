from yt_dlp import YoutubeDL, update
from cli_to_api import cli_to_api

class Downloader:

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
            'progress_hooks': [downloading_hook],
            'postprocessor_hooks': [done_hook]
        })

        with YoutubeDL(api_opt) as ytd:
            ytd.download(links)

    def check_updates(self):
        return update.Updater(YoutubeDL()).query_update() # TODO change this


def downloading_hook(d):
    if d['status'] == 'downloading':
        print(f"{d['downloaded_bytes'] / d['total_bytes'] * 100.0}%")
    elif d['status'] == 'finished':
        print("FINE DOWNLOAD")
    elif d['status'] == 'error':
        print("ERRORE")

def done_hook(d):
    if d['status'] == 'finished':
        print(d['postprocessor'], "-- FINITO!")

