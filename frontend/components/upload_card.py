import streamlit as st


def render_upload_card():

    st.subheader(" Upload Legal Document")

    st.write(
        "Upload a legal PDF to begin analysis. "
        "LexiScan will extract text, perform OCR if needed, "
        "build a searchable knowledge base, and prepare the document for AI analysis."
    )

    uploaded = st.file_uploader(
        "Choose a Legal PDF",
        type=["pdf"],
        help="Supported format: PDF"
    )

    if uploaded is None:
        st.info(
            "Supported documents: Contracts • NDAs • Lease Agreements • Sale Deeds • Court Documents"
        )

    return uploaded