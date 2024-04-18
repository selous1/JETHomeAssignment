#!/usr/bin/env bash

# Set up a virtual environment and install the required dependencies
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt

# Run main
python3 main.py

# Close virtual environment
deactivate