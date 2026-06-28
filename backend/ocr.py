import pytesseract
from pdf2image import convert_from_path

from backend.config import (
    TESSERACT_CMD,
    POPPLER_PATH
)


class OCRService:
    """
    OCR service for scanned PDFs using
    Tesseract + Poppler.
    """

    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD

    def extract_text(self, pdf_path):
        """
        Extract text from scanned PDFs.
        """

        pages = convert_from_path(
            pdf_path,
            poppler_path=POPPLER_PATH
        )

        text = ""

        for page in pages:
            page_text = pytesseract.image_to_string(page)
            text += page_text + "\n"

        return text