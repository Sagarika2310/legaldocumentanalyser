from langchain_openai import ChatOpenAI

from backend.config import OPENAI_API_KEY


class RAGEngine:

    def __init__(self, vector_store):

        self.vector_store = vector_store

        self.llm = ChatOpenAI(
            model="gpt-4.1-mini",
            temperature=0,
            api_key=OPENAI_API_KEY
        )

    def ask(self, question):

        docs = self.vector_store.similarity_search(
            question,
            k=4
        )

        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )

        prompt = f"""
You are an AI Legal Document Assistant.

Use ONLY the provided document context.

If the answer is not present, say:
"I could not find this information in the uploaded document."

Document Context:

{context}

Question:

{question}

Answer:
"""

        response = self.llm.invoke(prompt)

        return response.content