import fitz


def extract_text_from_pdf(pdf_path):
    """
    Extract embedded text using PyMuPDF.
    Returns:
        text (str)
        page_count (int)
    """

    document = fitz.open(pdf_path)

    page_count = len(document)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text, page_count