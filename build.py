import subprocess
import platform
import os
import sys

APP_NAME = "yt-dlp-GUI" 
MAIN_SCRIPT = "src/main.py"
ICON_WIN = "src/assets/icona.ico"
ICON_LINUX = "src/assets/icona.png"

RESOURCES = [
    ("src/assets", "assets"),
]

def compile():
    op_sis = platform.system()

    sep = ";" if op_sis == "Windows" else ":"
    icon = ICON_WIN if op_sis == "Windows" else ICON_LINUX

    data_params = []
    for src, dest in RESOURCES:
        data_params.extend(["--add-data", f"{src}{sep}{dest}"])

    command = [
        "pyinstaller",
        "--noconsole",
        "--onefile",
        f"--name={APP_NAME}",
        f"--icon={icon}",
        *data_params,
        MAIN_SCRIPT
    ]

    print(f"[*] Starting {APP_NAME} compilation...")
    try:
        subprocess.run(command, check=True)
        print("\n[+] Compilation completed successfully!")
        print("[*] You can find the executable at ", os.path.abspath("dist"))
    except subprocess.CalledProcessError:
        print("\n[-] Error during compilation.")
    except FileNotFoundError:
        print("\n[-] PyInstaller not found. Install with: pip install pyinstaller")

if __name__ == "__main__":
    compile()