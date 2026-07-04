from backend.prompts import (
    SUMMARY_PROMPT,
    CLAUSE_PROMPT,
    RISK_PROMPT
)


class LegalTools:

    def __init__(self, rag_engine):
        self.rag = rag_engine

    def summarize_document(self):
        return self.rag.ask(SUMMARY_PROMPT)

    def extract_clauses(self):
        return self.rag.ask(CLAUSE_PROMPT)

    def detect_risks(self):
        return self.rag.ask(RISK_PROMPT)

    def ask_question(self, question):
        return self.rag.ask(question)