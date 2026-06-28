from backend.ocr import OCRService

ocr = OCRService()

text = ocr.extract_text(
    "sample_documents/scanned_document.pdf"
)

print("=" * 50)
print(text[:1000])
print("=" * 50)