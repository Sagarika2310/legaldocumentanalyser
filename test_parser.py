from backend.parser import extract_text_from_pdf

pdf_path = r"C:\Users\SAGARIKA\OneDrive\Desktop\legal-document-analyzer\sample_documents\High_Risk_Sale_Deed_AI_Testing.pdf"

text = extract_text_from_pdf(pdf_path)

print(text[:3000])