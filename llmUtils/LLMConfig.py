from ast import List

from llama_cpp import llama_context_default_params, llama_model_default_params

class llmConfig:
    def __init__(self) -> None:
        self.modelPath:str = None
        self.prompt:str = ""
        self.params = None
        self.contextParams = None
        self.tokenPrompt = []
        pass
    def default(self) -> None:
        self.modelPath = "models/Llama-2-7B-GGUF/llama-2-7b.Q8_0.gguf"
        self.prompt = " Your name is call Jack-o"
        self.params = llama_model_default_params()
        self.contextParams = llama_context_default_params()
        return