import streamlit as st


def render_hero():

    with st.container(border=True):

        st.title("⚖️ LexiScan AI")

        st.subheader("AI-Powered Legal Document Intelligence")

        st.write(
            """
Upload legal documents, extract text using OCR, build an intelligent
knowledge base using Retrieval-Augmented Generation (RAG), and interact
naturally with your documents through AI-powered legal assistance.
"""
        )

        c1, c2, c3, c4 = st.columns(4)

        c1.metric("OCR", "✓")
        c2.metric("RAG", "✓")
        c3.metric("LangGraph", "✓")
        c4.metric("FAISS", "✓")

    st.markdown("")