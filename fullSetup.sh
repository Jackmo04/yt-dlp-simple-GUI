#!/bin/bash

if [[ ! -d '.venv' ]]; then
    echo "[*] Creating virtual environment..." &&
    python3 -m venv .venv &&
    echo "[+] Virtual environment created at .venv" &&
    source .venv/bin/activate &&
    echo "[*] Installing dependencies..." &&
    pip install -r requirements.txt &&
    echo "[+] Dependencies installed" &&
    echo "[*] Installing PyInstaller..." &&
    pip install pyinstaller &&
    echo "[+] PyInstaller installed" &&
    echo "[*] Compiling the application..." &&
    python3 ./build.py &&
    deactivate &&
    mkdir bin/ &&
    mv dist/* ./bin/ &&
    echo "[*] Cleaning up build artifacts..." &&
    rm -rf .venv build dist __pycache__ *.spec &&
    chmod +x ytdlpGUI &&
    echo "[+] Application compiled and ready to use!"
    echo "[*] You can find the compiled application in the 'bin' directory."
else
    echo "[!] The environment is already set up."
fi
