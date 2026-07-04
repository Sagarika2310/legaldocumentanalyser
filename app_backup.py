from backend.file_handler import save_uploaded_file
from backend.document_processor import DocumentProcessor
import streamlit as st

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Legal Document Analyzer",
    page_icon="⚖️",
    layout="wide"
)

# -------------------------------
# Sidebar
# -------------------------------
with st.sidebar:
    st.title("⚖️ Legal Document Analyzer")

    st.markdown("---")

    st.subheader("📂 Upload Document")

    uploaded_file = st.file_uploader(
        "Choose a Legal PDF",
        type=["pdf"]
    )

    st.markdown("---")

    st.subheader("🛠 Analysis Options")

    analysis_type = st.radio(
        "Select Analysis",
        [
            "Document Summary",
            "Clause Extraction",
            "Risk Detection",
            "Ask Questions"
        ]
    )

    st.markdown("---")

    st.subheader("ℹ️ Document Status")

    if uploaded_file:
        st.success("Document Uploaded Successfully!")
        st.write(f"📄 {uploaded_file.name}")

        # Save uploaded file
        file_path = save_uploaded_file(uploaded_file)

        from backend.document_processor import DocumentProcessor

        processor = DocumentProcessor()

        result = processor.process_document(file_path)

        extracted_text = result["text"]
        metadata = result["metadata"]

        st.session_state["document_text"] = extracted_text
        st.session_state["metadata"] = metadata

        st.divider()

        st.subheader("📄 Extracted Text Preview")

        st.text_area(
            "Preview",
            extracted_text[:3000],
            height=250
        )
    if "metadata" in st.session_state:

        st.divider()

        st.subheader("📊 Document Metadata")

        metadata = st.session_state["metadata"]

        st.write(f"**Filename:** {metadata['filename']}")
        st.write(f"**Words:** {metadata['word_count']}")
        st.write(f"**Characters:** {metadata['character_count']}")
        st.write(f"**Method:** {metadata['processing_method']}")
        st.write(f"**OCR Used:** {'Yes' if metadata['ocr_used'] else 'No'}")
        st.write(f"**Processing Time:** {metadata['processing_time']} sec")
    else:
            st.info("No document uploaded")

        # -------------------------------
        # Main Page
        # -------------------------------

    st.title("⚖️ AI Legal Document Analyzer")

    st.write(
            """
            Upload a legal document and interact with it using AI.

            ### Features
            - 📄 Document Summarization
            - 📑 Clause Extraction
            - ⚠️ Risk Detection
            - 💬 Legal Question Answering (RAG)
            """
        )

    st.divider()

        # -------------------------------
        # Chat Section
        # -------------------------------

    st.subheader("💬 Chat with your Document")

        # Initialize chat history
    if "messages" not in st.session_state:
            st.session_state.messages = []

            # Display previous messages
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

                    # Chat input
                    prompt = st.chat_input("Ask a legal question...")

                    if prompt:

                        # Show user message
                        st.session_state.messages.append(
                            {
                                "role": "user",
                                "content": prompt
                            }
                        )

                        with st.chat_message("user"):
                            st.markdown(prompt)

                            # Placeholder AI response
                            response = (
                                "This is a placeholder response.\n\n"
                                "The OpenAI-powered Legal Document Analyzer will answer your questions here in the next phase."
                            )

                            st.session_state.messages.append(
                                {
                                    "role": "assistant",
                                    "content": response
                                }
                            )

                            with st.chat_message("assistant"):
                                st.markdown(response)