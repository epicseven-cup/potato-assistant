class Message:
    def __init__(self, userRole, userContent) -> None:
        self.chat = {"role": userRole, "content": userContent}
        pass