#!/bin/bash

# Create the virtual environment
echo " Create the .venv"
python -m venv .venv

# Activate it
echo "Activating the environment. . ."
# Only done for windows based system. Will be impoved in the future.
source "$(pwd)/.venv/Scripts/activate"

# Install latest pip
python -m pip install --upgrade pip

# Install pipreqs for requirements
pip install pipreqs

# Create the requirements.txt
pipreqs . --force --encoding=utf-8 --ignore .venv,.git

# Installing dependencies in the env
pip install -r requirements.txt

# Print the ending message in red
echo -e "\033[0;m Setup Completed!\033[0m"