from backend.document_processor import DocumentProcessor

processor = DocumentProcessor()

result = processor.process_document(
    "sample_documents/High_Risk_Sale_Deed_AI_Testing.pdf"
)

print(type(result))
print(result.keys())

print("\nMetadata:")
print(result["metadata"])

print("\nText Preview:")
print(result["text"][:500])