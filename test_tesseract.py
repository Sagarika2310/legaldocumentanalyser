import pytesseract
from PIL import Image

from backend.config import TESSERACT_CMD

# Tell pytesseract where Tesseract is installed
pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD

print("Tesseract Version:")
print(pytesseract.get_tesseract_version())