from ast import List
from typing import Iterator
from llama_cpp import CreateChatCompletionResponse, CreateChatCompletionStreamResponse, Llama
from llmUtils.LLMConfig import llmConfig
from queue import Queue
from utils.Message import message

class llmBrain:
    def __init__(self, config:llmConfig) -> None:
        self.config:llmConfig = config
        print(self.config.modelPath)
        self.llm:Llama = Llama(model_path=self.config.modelPath, chat_format="llama-2")
        self.messageQueue:Queue[message] = Queue()
        pass
    def appendingMessage(self, message: message):
        self.messageQueue.put(message)                                                                                              
        pass
    def generate(self):
        messageObject:message = self.messageQueue.get()
        messageToken = messageObject.tokenize(self)
        print(messageToken)
        tokens = self.llm.generate(messageToken)
        print(len(tokens))
        return ""