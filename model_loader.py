import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from config import *

def create_bnb_config():
    """Configures model quantization method using bitsandbytes"""
    compute_dtype_map = {
        "bfloat16": torch.bfloat16,
        "float16": torch.float16,
        "float32": torch.float32
    }
    
    return BitsAndBytesConfig(
        load_in_4bit=LOAD_IN_4BIT,
        bnb_4bit_use_double_quant=BNB_4BIT_USE_DOUBLE_QUANT,
        bnb_4bit_quant_type=BNB_4BIT_QUANT_TYPE,
        bnb_4bit_compute_dtype=compute_dtype_map.get(BNB_4BIT_COMPUTE_DTYPE, torch.bfloat16),
    )

def load_model():
    """Loads model and model tokenizer with authentication"""
    # Login to Hugging Face first
    from huggingface_hub import login
    login(token=HF_TOKEN)  # Uses the token from config.py

    # Get number of GPU device and set maximum memory
    n_gpus = torch.cuda.device_count()
    max_memory = f'{40960}MB'

    # Load model
    bnb_config = create_bnb_config()
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        quantization_config=bnb_config,
        device_map="auto",
        max_memory={i: max_memory for i in range(n_gpus)},
        use_auth_token=True  # Important for gated models
    )

    # Load tokenizer
    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_NAME,
        use_auth_token=True  # Important for gated models
    )
    tokenizer.pad_token = tokenizer.eos_token

    return model, tokenizer
