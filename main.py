from model_loader import load_model
from api_server import APIServer
from config import DEVICE
import torch

def main():
    # Load model and tokenizer
    model, tokenizer = load_model()
    
    # Create and run API server
    server = APIServer(tokenizer, model, DEVICE)
    server.run()

if __name__ == "__main__":
    main()
