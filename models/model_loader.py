import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

class ModelLoader:
    """
    A class to handle loading of a pre-trained model and tokenizer.
    """
    def __init__(self, model_name: str, bnb_config, max_memory_mb: int = 40960):
        """
        Initialize the ModelLoader.

        Args:
            model_name (str): Hugging Face model name.
            bnb_config: BitsAndBytes quantization configuration.
            max_memory_mb (int): Maximum memory per GPU in MB.
        """
        self.model_name = model_name
        self.bnb_config = bnb_config
        self.max_memory_mb = max_memory_mb
        self.model = None
        self.tokenizer = None

    def load(self, use_auth_token: bool = True):
        """
        Loads the model and tokenizer.

        Args:
            use_auth_token (bool): Use Hugging Face authentication token.

        Returns:
            tuple: (model, tokenizer)
        """
        n_gpus = torch.cuda.device_count()
        max_memory = {i: f"{self.max_memory_mb}MB" for i in range(n_gpus)}

        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            quantization_config=self.bnb_config,
            device_map="auto",
            max_memory=max_memory,
        )

        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_name,
            use_auth_token=use_auth_token
        )
        self.tokenizer.pad_token = self.tokenizer.eos_token

        return self.model, self.tokenizer