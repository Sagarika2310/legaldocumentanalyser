from backend.memory import MemoryManager
from backend.tools import LegalTools


class LegalAgent:
    """
    Legal AI Agent

    Uses:
    - LangChain Memory
    - Legal Tools
    - RAG
    """

    def __init__(self, rag_engine):

        self.memory = MemoryManager()

        self.tools = LegalTools(rag_engine)

    def chat(self, question):

        self.memory.add_user_message(question)

        response = self.tools.ask_question(question)

        self.memory.add_ai_message(response)

        return response

    def summarize(self):
        return self.tools.summarize_document()

    def clauses(self):
        return self.tools.extract_clauses()

    def risks(self):
        return self.tools.detect_risks()

    def history(self):
        return self.memory.get_history()

    def clear_history(self):
        self.memory.clear()