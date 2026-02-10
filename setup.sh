#!/bin/bash

if [[ ! -d '.venv' ]]; then
    echo "[*] Creating virtual environment..."
    python3 -m venv .venv
    echo "[+] Virtual environment created at .venv"
    source .venv/bin/activate
    echo "[*] Installing dependencies..."
    pip install -r requirements.txt
    echo "[+] Dependencies installed"
    deactivate
    echo "[+] All done!"
else
    echo "[!] The environment is already set up."
    echo "[*] You can start the application by running './run.sh'"
fi
