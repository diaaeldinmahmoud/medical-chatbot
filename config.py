# Configuration constants
HF_TOKEN = "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"
NGROK_AUTH_TOKEN = "2vkPuMmd9UPu6pysv3XjV6zELCa_7ewiJDZG36KMXWaQYWftb"

# Model configuration
MODEL_NAME = "CohereForAI/c4ai-command-r7b-arabic-02-2025"

# bitsandbytes parameters
LOAD_IN_4BIT = True
BNB_4BIT_USE_DOUBLE_QUANT = True
BNB_4BIT_QUANT_TYPE = "nf4"
BNB_4BIT_COMPUTE_DTYPE = "bfloat16"  # Changed from "torch.bfloat16"

# Device configuration
DEVICE = "cuda"
TORCH_DTYPE = "float16"  # Changed from "torch.float16"
