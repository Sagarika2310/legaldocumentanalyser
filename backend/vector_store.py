from langchain_community.vectorstores import FAISS

from backend.embeddings import EmbeddingService


class VectorStore:

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.db = None

    def create_vector_store(self, chunks):
        """
        Create FAISS vector database from document chunks.
        """

        self.db = FAISS.from_texts(
            texts=chunks,
            embedding=self.embedding_service.embeddings
        )

        return self.db

    def similarity_search(
        self,
        query,
        k=4
    ):
        """
        Retrieve the most relevant chunks.
        """

        if self.db is None:
            raise ValueError(
                "Vector database has not been created."
            )

        return self.db.similarity_search(
            query,
            k=k
        )