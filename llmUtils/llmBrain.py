from ast import List
from llama_cpp import Llama
from llmConfig import llmConfig
from queue import Queue
from utils.message import Message

class llmBrain:
    def __init__(self, config:llmConfig) -> None:
        self.config:llmConfig = config
        self.llm:Llama = Llama(model_path=self.config.modelPath)
        self.messageQueue:Queue[Message] = Queue()
        pass
    def appendingMessage(self, message: Message):
        self.messageQueue.put(message)
        pass
    def generate(self, message: Message) -> List[int]:
        output = self.llm.create_chat_completion(messages=message)
        pass