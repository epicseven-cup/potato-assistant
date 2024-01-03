

class message:
    def __init__(self, userRole, userContent) -> None:
        self.chat = {"role": userRole, "content": userContent}
    def computeChatCompletion(self, prompt):
        return [prompt, self.chat]
    def tokenize(self, llm):
        text:str = f"{self.chat.get('role', 'User')}: {self.chat.get('content', 'There is no text here, please repeat this line')} "
        return llm.llm.tokenize(text.encode("utf-8"))