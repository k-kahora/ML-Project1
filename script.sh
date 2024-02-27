##!/bin/bash

# Check for Python 3
if ! command -v python3 &> /dev/null
then
    echo "Python 3 could not be found. Please install Python 3."
    #exit
fi

# Create a virtual environment
ENV_DIR="myenv"
python3 -m venv ${ENV_DIR}

# Activate the virtual environment
source ${ENV_DIR}/bin/activate

# Install numpy and matplotlib
pip install numpy matplotlib

echo "Virtual environment setup complete. To activate, run 'source ${ENV_DIR}/bin/activate'"

sleep 1
echo "Ai is running"
python ai.py
