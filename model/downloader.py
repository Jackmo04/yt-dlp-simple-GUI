from yt_dlp import YoutubeDL
from model.utils.cli_to_api import cli_to_api
from pathlib import Path

class Downloader:

    def __init__(self):
        self.progress_hook = None
        self.postprocessing_hook = None

    def download_audio(self, links : list, dest=Path.home() / "Downloads", playlist=False):
        self.download(links, ['-t', 'mp3'], dest, playlist)

    def download_video(self, links : list, dest=Path.home() / "Downloads", playlist=False):
        self.download(links, ['-t', 'mp4'], dest, playlist)

    def download(self, links : list, options : list, dest=Path.home() / "Downloads", playlist=False):
        actual_dest = dest / "%(title)s.%(ext)s"
        cli_opt = options + [
            '-o', str(actual_dest),
            '--yes-playlist' if playlist else '--no-playlist',
            "--embed-thumbnail",
            "--quiet"
        ]

        api_opt = cli_to_api(cli_opt)

        with YoutubeDL(api_opt) as ytd:
            if self.progress_hook is not None:
                ytd.add_progress_hook(self.progress_hook)
            if self.postprocessing_hook is not None:
                ytd.add_postprocessor_hook(self.postprocessing_hook)
            ytd.download(links)

    def set_progress_hook(self, hook):
        self.progress_hook = hook

    def set_postprocessing_hook(self, hook):
        self.postprocessing_hook = hook

