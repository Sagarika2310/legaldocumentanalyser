import os
import time

from backend.parser import extract_text_from_pdf
from backend.ocr import OCRService


class DocumentProcessor:
    """
    Complete document processing pipeline.
    """

    def __init__(self):
        self.ocr = OCRService()

    def process_document(self, file_path):
        start_time = time.time()

        # Try extracting embedded text
        text = extract_text_from_pdf(file_path)

        ocr_used = False

        # OCR fallback
        if not text or len(text.strip()) < 100:
            print("[INFO] No embedded text found.")
            print("[INFO] Running OCR...")

            text = self.ocr.extract_text(file_path)
            ocr_used = True

        # Safety check
        if text is None:
            text = ""

        processing_method = (
            "OCR (Tesseract)"
            if ocr_used
            else "PyMuPDF Text Extraction"
        )

        metadata = {
            "filename": os.path.basename(file_path),
            "character_count": len(text),
            "word_count": len(text.split()),
            "processing_method": processing_method,
            "ocr_used": ocr_used,
            "processing_time": round(time.time() - start_time, 2),
        }

        return {
            "text": text,
            "metadata": metadata,
        }