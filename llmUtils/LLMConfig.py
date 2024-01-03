from ast import List

class llmConfig:
    def __init__(self) -> None:
        self.modelPath:str = None
        self.prompt:str = ""
        self.tokenPrompt = []
        pass
    def default(self) -> None:
        self.modelPath = ""
        self.prompt = ""