import torch
from transformers import BitsAndBytesConfig

def create_bnb_config(
    load_in_4bit: bool = True,
    bnb_4bit_use_double_quant: bool = True,
    bnb_4bit_quant_type: str = "nf4",
    bnb_4bit_compute_dtype: torch.dtype = torch.bfloat16
) -> BitsAndBytesConfig:
    """
    Creates a BitsAndBytes configuration for 4-bit quantization.

    Args:
        load_in_4bit (bool): Enable 4-bit precision loading.
        bnb_4bit_use_double_quant (bool): Enable nested quantization.
        bnb_4bit_quant_type (str): Quantization type ('fp4' or 'nf4').
        bnb_4bit_compute_dtype (torch.dtype): Computation data type.

    Returns:
        BitsAndBytesConfig: Configured quantization object.
    """
    return BitsAndBytesConfig(
        load_in_4bit=load_in_4bit,
        bnb_4bit_use_double_quant=bnb_4bit_use_double_quant,
        bnb_4bit_quant_type=bnb_4bit_quant_type,
        bnb_4bit_compute_dtype=bnb_4bit_compute_dtype,
    )