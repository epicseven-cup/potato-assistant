from llmUtils.LLMConfig import llmConfig
from llmUtils.LLMBrain import llmBrain
from utils.Message import message
def main():
    config = llmConfig()
    config.default()
    llm:llmBrain = llmBrain(config=config)
    testMessage = message(userRole="user", userContent="What is your name?")
    llm.appendingMessage(testMessage)
    output = llm.generate()
    print(output)
    return

if __name__ == "__main__":
    main()