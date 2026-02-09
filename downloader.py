from yt_dlp import YoutubeDL
from cli_to_api import cli_to_api

def my_hook(d):
    if d['status'] == 'finished':
        print("HOOK ATTIVATO!")

URL = ["https://www.youtube.com/watch?v=9ruLQ1Hmhjs"]
opt = cli_to_api(["-t", "mp3", "--embed-thumbnail", "-o", "~/Downloads/%(title)s.%(ext)s"])
opt.update({'progress_hooks': [my_hook]})

with YoutubeDL(opt) as ytd:
    ytd.download(URL)

