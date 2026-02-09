import subprocess
import sys
import os

def executeProgram(subdir : str, script_name : str, script_args : list):

    command = [script_name] + script_args
    abs_subdir = os.path.abspath(subdir)

    print(f"Running: {command}")

    try:
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            cwd=abs_subdir
        )

        # Leggiamo l'output riga per riga
        while True:
            line = process.stdout.readline()
            if not line and process.poll() is not None:
                # Se la riga è vuota e il processo è terminato (poll != None), usciamo
                break
            if line:
                print(f"{line}", end="")
                sys.stdout.flush()

        # Cruciale: attendiamo che il processo termini effettivamente
        return_code = process.wait()
        
        # Questa riga deve essere stampata
        print(f"\n--- Processo terminato con status code: {return_code} ---")
        return return_code
    
    except FileNotFoundError:
        print(f"Errore: Assicurati che '{script_name}' esista in '{subdir}'")
        return 1
    
def downloadAudio(link, playlist=False):
    args = ["--yes-playlist"] if playlist else ["--no-playlist"]
    args += ["-t", "mp3", link]
    yt_dlp(args)

def downloadVideo(link, playlist=False):
    args = ["--yes-playlist"] if playlist else ["--no-playlist"]
    args += ["-t", "mp4", link]
    yt_dlp(args)

def yt_dlp(args):
    executeProgram("bin", "yt-dlp", args)

