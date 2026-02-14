#!/bin/bash

FIRST_RUN=false

if [[ ! -d ".venv" ]]; then
    FIRST_RUN=true
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

source .venv/bin/activate

if $FIRST_RUN; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
fi

python3 src/main.py

deactivate
