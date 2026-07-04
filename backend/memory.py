from langchain_core.chat_history import InMemoryChatMessageHistory


class MemoryManager:
    """
    Modern LangChain 1.x memory implementation.
    """

    def __init__(self):
        self.history = InMemoryChatMessageHistory()

    def add_user_message(self, message):
        self.history.add_user_message(message)

    def add_ai_message(self, message):
        self.history.add_ai_message(message)

    def get_history(self):
        return self.history.messages

    def clear(self):
        self.history.clear()