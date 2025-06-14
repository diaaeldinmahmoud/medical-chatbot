import os
import sys
import torch
import subprocess
from google.colab import userdata
from config.quantization_config import create_bnb_config
from models.model_loader import ModelLoader
from utils.environment_setup import install_dependencies, authenticate_huggingface

def main():
    """
    Main function to set up the environment, clone the repository, and load the model.
    """
    try:
        # Clone the GitHub repository
        repo_url = "https://github.com/diaaeldinmahmoud/medical-nlp-project.git"
        subprocess.run(f"git clone {repo_url}", shell=True, check=True)
        os.chdir("/content/medical-nlp-project")

        # Add project directory to Python path
        sys.path.append("/content/medical-nlp-project")

        # Set device and data type
        device = "cuda"
        torch_dtype = torch.bfloat16

        # Install dependencies
        print("Installing dependencies...")
        install_dependencies()

        # Authenticate with Hugging Face
        print("Authenticating with Hugging Face...")
        hf_token = userdata.get("HF_TOKEN")
        if not hf_token:
            raise ValueError("HF_TOKEN not found in Colab secrets. Please set it in the Secrets tab.")
        authenticate_huggingface(hf_token)

        # Define model and quantization parameters
        model_name = "CohereForAI/c4ai-command-r7b-arabic-02-2025"
        bnb_config = create_bnb_config(
            load_in_4bit=True,
            bnb_4bit_use_double_quant=True,
            bnb_4bit_quant_type="nf4",
            bnb_4bit_compute_dtype=torch.bfloat16
        )

        # Load model and tokenizer
        print("Loading model and tokenizer...")
        loader = ModelLoader(model_name, bnb_config)
        model, tokenizer = loader.load()

        print("Model and tokenizer loaded successfully.")
        print(f"Model device: {model.device}")
        print(f"Tokenizer pad_token equals eos_token: {tokenizer.pad_token == tokenizer.eos_token}")

        # Make model and tokenizer available globally for interactive use
        globals()['model'] = model
        globals()['tokenizer'] = tokenizer

        return model, tokenizer

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    model, tokenizer = main()