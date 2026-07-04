from backend.document_processor import DocumentProcessor
from backend.chunking import DocumentChunker
from backend.vector_store import VectorStore

processor = DocumentProcessor()

result = processor.process_document(
    "sample_documents/High_Risk_Sale_Deed_AI_Testing.pdf"
)

text = result["text"]

chunker = DocumentChunker()

chunks = chunker.split_text(text)

vector_db = VectorStore()

vector_db.create_vector_store(chunks)

results = vector_db.similarity_search(
    "termination clause"
)

print("=" * 60)

for i, doc in enumerate(results):

    print(f"\nResult {i+1}\n")

    print(doc.page_content[:600])

    print("-" * 60)