#!/bin/bash

if [[ ! -d '.venv' ]]; then
    ./setup.sh
fi

source .venv/bin/activate
python3 ./main.py
deactivate
