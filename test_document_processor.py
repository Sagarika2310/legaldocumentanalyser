from backend.document_processor import DocumentProcessor

processor = DocumentProcessor()

result = processor.process_document(
    "sample_documents\High_Risk_Sale_Deed_AI_Testing.pdf"
)

print("\n========= METADATA =========")
print(result["metadata"])

print("\n========= TEXT PREVIEW =========\n")
print(result["text"][:1000])