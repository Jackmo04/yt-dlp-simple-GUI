#!/bin/bash

if [[ ! -d '.venv' ]]; then
    echo "[*] Creating virtual environment..."
    python3 -m venv .venv
    echo "[+] Virtual environment created at .venv"
    source .venv/bin/activate
    echo "[*] Installing packages..."
    pip install -r requirements.txt
    echo "[+] Packages installed"
    deactivate
    echo "[+] All done!"
fi
