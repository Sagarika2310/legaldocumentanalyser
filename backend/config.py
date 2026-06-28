import os
from dotenv import load_dotenv

load_dotenv()

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Upload directory
UPLOAD_FOLDER = "uploads"

# Tesseract executable path
TESSERACT_CMD = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Poppler bin folder
POPPLER_PATH = (
    r"C:\Users\SAGARIKA\Downloads\Release-26.02.0-0"
    r"\poppler-26.02.0\Library\bin"
)