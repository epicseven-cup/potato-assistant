from ast import List
from typing import Iterator
from llama_cpp import llama_new_context_with_model, llama_token, llama_token_get_text, llama_token_to_piece, llama_tokenize, c_size_t, llama_load_model_from_file, llama_n_ctx, llama_model_p, llama_context_p, llama_backend_init
from llmUtils.LLMConfig import llmConfig
from queue import Queue
from utils.Message import message


# New order should be [llmConfig, llmBrain] -> llmSession that contains the models session

class llmBrain:
    def __init__(self, config:llmConfig) -> None:
        self.config:llmConfig = config
        llama_backend_init(numa=False)
        self.ctx:llama_context_p = llama_new_context_with_model(self.llm, config.contextParams)
        self.nctx:int = llama_n_ctx(self.ctx)
        self.model:llama_model_p = llama_load_model_from_file(path_model=config.modelPath.encode("utf-8"), params=config.params)
        self.messageQueue:Queue[message] = Queue()
        self.promptToken = self.computePromptToken()
        self.n_next_max = 30
        self.n_next = min(self.n_next_max, self.nctx - len(self.promptToken))
        pass
    def createNewSession(self):
        pass
    def loadSession(self):
        pass
    def cacheItemSession(self):
        pass
    def appendingMessage(self, message: message):
        self.messageQueue.put(message)                                                 
        pass
    def computePromptToken(self):
        promptToken = (llama_token * (len(self.config.prompt) + 1))()
        tokenCount = c_size_t()
        tokenCutOff = llama_tokenize(model=self.model, text=self.config.prompt, text_len=len(promptToken), tokens=promptToken, n_max_tokens=len(promptToken), add_bos=False, special=False)
        promptToken = promptToken[:tokenCutOff]
        return promptToken
    def generate(self):
        messageObject:message = self.messageQueue.get()
        tokenContent = ""
        return ""