#!/bin/bash

FIRST_RUN=false

if [[ ! -d ".venv" ]]; then
    FIRST_RUN=true
    python3 -m venv .venv
fi

source .venv/bin/activate

if $FIRST_RUN; then
    pip install -r requirements.txt
fi

python3 src/main.py

deactivate
