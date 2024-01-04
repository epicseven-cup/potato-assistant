from ast import List
from typing import Iterator
from llama_cpp import llama_new_context_with_model, llama_token, llama_token_get_text, llama_token_to_piece, llama_tokenize, llama_load_model_from_file, llama_n_ctx, llama_model_p, llama_context_p
from llmUtils.LLMConfig import llmConfig
from queue import Queue
from utils.Message import message

class llmBrain:
    def __init__(self, config:llmConfig) -> None:
        self.config:llmConfig = config
        print(self.config.modelPath)
        self.llm:llama_model_p = llama_load_model_from_file(path_model=config.modelPath.encode("utf-8"), params=config.params)
        self.ctx:llama_context_p = llama_new_context_with_model(self.llm, config.contextParams)
        self.nctx:int = llama_n_ctx(self.ctx)
        self.messageQueue:Queue[message] = Queue()
        pass
    def appendingMessage(self, message: message):
        self.messageQueue.put(message)                                                                                              
        pass
    def generate(self):
        messageObject:message = self.messageQueue.get()
        tokenContent = messageObject.tokenize(self)
        print(tokenContent)
        respond = messageObject.detokenize(self)
        print(respond)
        return ""