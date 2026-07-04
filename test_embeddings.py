from backend.document_processor import DocumentProcessor
from backend.chunking import DocumentChunker
from backend.embeddings import EmbeddingService

processor = DocumentProcessor()

result = processor.process_document(
    "sample_documents/High_Risk_Sale_Deed_AI_Testing.pdf"
)

text = result["text"]

chunker = DocumentChunker()
chunks = chunker.split_text(text)

embedding_service = EmbeddingService()

embeddings = embedding_service.create_embeddings(chunks)

print("=" * 60)
print("Total Chunks:", len(chunks))
print("Total Embeddings:", len(embeddings))
print("Embedding Dimension:", len(embeddings[0]))
print("=" * 60)