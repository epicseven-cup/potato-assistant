from llama_cpp import llama_token, llama_token_get_text, llama_tokenize

# from llmUtils.LLMBrain import llmBrain


class message:
    def __init__(self, userRole, userContent) -> None:
        self.role = userRole
        self.content = userContent.encode("utf-8")
    def computeChatCompletion(self, prompt):
        return [prompt, self.chat]
    def tokenize(self, llm):
        # C int array
        output = (llama_token * llm.nctx)()
        # converts the user given content into token so I can feed it to the llm 
        messageTokenEnd = llama_tokenize(model=llm.llm,  text=self.content, tokens=output, text_len=len(self.content), n_max_tokens=llm.nctx, add_bos=False, special=True)
        return output[:messageTokenEnd]
    def detokenize(self, llm):
        output = self.tokenize(llm)
        respond = b""
        for i in output:
            character = llama_token_get_text(llm.llm, i)
            respond = respond + character
        return respond