from backend.document_processor import DocumentProcessor
from backend.chunking import DocumentChunker
from backend.vector_store import VectorStore
from backend.rag import RAGEngine
from backend.tools import LegalTools

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

tools = LegalTools(rag)

print("=" * 60)
print("DOCUMENT SUMMARY")
print("=" * 60)
print(tools.summarize_document())

print("=" * 60)
print("CLAUSES")
print("=" * 60)
print(tools.extract_clauses())

print("=" * 60)
print("RISKS")
print("=" * 60)
print(tools.detect_risks())