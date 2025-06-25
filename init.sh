#!/bin/bash

# Create the virtual environment
echo " Create the .venv"
python -m venv .venv

# Activate it
echo "Activating the environment. . ."
source .venv/bin/activate

# Install pipreqs for requirements
pip install pipreqs

# Create the requirements.txt
pipreqs --force .

# Installing dependencies in the env
pip install -r requirements.txt

# Print the ending message in red
echo -e "\033[0;m Setup Completed!\033[0m"