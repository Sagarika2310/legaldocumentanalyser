from backend.document_processor import DocumentProcessor
from backend.chunking import DocumentChunker

processor = DocumentProcessor()

result = processor.process_document(
    "sample_documents/High_Risk_Sale_Deed_AI_Testing.pdf"
)

text = result["text"]

chunker = DocumentChunker()

chunks = chunker.split_text(text)

print("=" * 50)
print("Total Chunks:", len(chunks))
print("=" * 50)

for i, chunk in enumerate(chunks[:3]):
    print(f"\nChunk {i+1}\n")
    print(chunk[:500])
    print("-" * 60)