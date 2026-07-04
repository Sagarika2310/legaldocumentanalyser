from langchain_openai import OpenAIEmbeddings
from backend.config import OPENAI_API_KEY


class EmbeddingService:
    """
    Generates OpenAI embeddings for
    document chunks.
    """

    def __init__(self):
        self.embeddings = OpenAIEmbeddings(
            model="text-embedding-3-small",
            api_key=OPENAI_API_KEY
        )

    def create_embeddings(self, chunks):
        """
        Generate embeddings for all chunks.
        """

        return self.embeddings.embed_documents(chunks)

    def create_query_embedding(self, query):
        """
        Generate embedding for user query.
        """

        return self.embeddings.embed_query(query)