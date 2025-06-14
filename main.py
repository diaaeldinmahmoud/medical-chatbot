import os
import sys
import torch
import subprocess
try:
    from google.colab import userdata
    IN_COLAB = True
except ImportError:
    IN_COLAB = False

def main():
    """
    Main function to set up the environment, clone the repository, and load the model.
    """
    try:
        if not IN_COLAB:
            raise RuntimeError("This script is designed to run in Google Colab.")

        # Clone the GitHub repository
        repo_url = "https://github.com/diaaeldinmahmoud/medical-nlp-project.git"
        clone_dir = "/content/medical-nlp-project"
        print(f"Cloning repository: {repo_url}")
        if os.path.exists(clone_dir):
            print(f"Directory {clone_dir} already exists, removing it...")
            subprocess.run(f"rm -rf {clone_dir}", shell=True, check=True)
        subprocess.run(f"git clone {repo_url} {clone_dir}", shell=True, check=True)
        os.chdir(clone_dir)

        # Verify directory structure
        required_dirs = ["config", "models", "utils"]
        for d in required_dirs:
            if not os.path.exists(d):
                raise FileNotFoundError(f"Directory {d} not found in {clone_dir}")
        if not os.path.exists("config/quantization_config.py"):
            raise FileNotFoundError("quantization_config.py not found in config/")

        # Add project directory to Python path
        sys.path.append(clone_dir)
        print(f"Python path updated: {sys.path}")

        # Import modules after path update
        from config.quantization_config import create_bnb_config
        from models.model_loader import ModelLoader
        from utils.environment_setup import install_dependencies, authenticate_huggingface

        # Set device and data type
        device = "cuda"
        torch_dtype = torch.bfloat16

        # Install dependencies
        print("Installing dependencies...")
        install_dependencies()

        # Authenticate with Hugging Face
        print("Authenticating with Hugging Face...")
        hf_token = None
        if IN_COLAB:
            try:
                hf_token = userdata.get("HF_TOKEN")
            except Exception as e:
                print(f"Warning: Failed to get HF_TOKEN from Colab secrets: {e}")
        if not hf_token:
            hf_token = os.getenv("HF_TOKEN")
        if not hf_token:
            raise ValueError("HF_TOKEN not found. Set it in Colab secrets or environment variable.")
        authenticate_huggingface(hf_token)

        # Define model and quantization parameters
        model_name = "meta-llama/Llama-2-7b-hf"  # Replaced due to potential unavailability
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

        # Make model and tokenizer available globally
        globals()['model'] = model
        globals()['tokenizer'] = tokenizer

        return model, tokenizer

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    model, tokenizer = main()
