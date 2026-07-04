from backend.document_processor import DocumentProcessor
from backend.chunking import DocumentChunker
from backend.vector_store import VectorStore
from backend.rag import RAGEngine

processor = DocumentProcessor()

result = processor.process_document(
    "sample_documents/High_Risk_Sale_Deed_AI_Testing.pdf"
)

text = result["text"]

chunker = DocumentChunker()

chunks = chunker.split_text(text)

vector_db = VectorStore()

vector_db.create_vector_store(chunks)

rag = RAGEngine(vector_db)

question = "Who are the parties involved in this agreement?"

answer = rag.ask(question)

print("=" * 60)
print(question)
print("=" * 60)
print(answer)