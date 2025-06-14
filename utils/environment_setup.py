import os
import subprocess

def install_dependencies():
    """
    Installs required Python libraries for the project.
    """
    commands = [
        "pip install pydantic",
        "pip install --upgrade transformers",
        "pip uninstall -y bitsandbytes",
        "pip install bitsandbytes",
        "pip install -q accelerate==0.26.0 --progress-bar off",
        "pip install --upgrade accelerate",
        "pip install datasets",
    ]
    
    for cmd in commands:
        subprocess.run(cmd, shell=True, check=True)

def authenticate_huggingface(hf_token: str):
    """
    Authenticates with Hugging Face using the provided token.

    Args:
        hf_token (str): Hugging Face API token.
    """
    subprocess.run(f"huggingface-cli login --token {hf_token}", shell=True, check=True)