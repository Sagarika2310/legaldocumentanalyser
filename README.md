# ⚖️ LexiScan AI
### AI-Powered Legal Document Analyzer using LangGraph, RAG & OCR

LexiScan AI is an intelligent Legal Document Analysis platform that simplifies the understanding of legal documents using Artificial Intelligence.

The application extracts text from both searchable and scanned legal PDFs, builds a semantic knowledge base using Retrieval-Augmented Generation (RAG), and enables users to summarize documents, extract important clauses, identify potential legal risks, and interact with documents through an AI-powered conversational assistant.

---

# 📌 Features

- 📄 Upload legal PDF documents
- 🔍 Automatic OCR fallback for scanned documents
- 📚 Intelligent document chunking
- 🧠 Semantic search using FAISS Vector Database
- 🤖 LangGraph-powered AI workflow
- 📄 AI-generated document summaries
- 📑 Automatic clause extraction
- ⚠️ Legal risk detection
- 💬 Conversational Legal AI Assistant
- 📊 Document Health Dashboard

---

# 🏗️ System Architecture

```
                    User
                      │
                      ▼
             Streamlit Frontend
                      │
              Upload Legal PDF
                      │
                      ▼
          Document Processing Layer
          ├── PyMuPDF Text Extraction
          └── OCR (Tesseract)
                      │
                      ▼
             Document Chunking
                      │
                      ▼
             OpenAI Embeddings
                      │
                      ▼
             FAISS Vector Store
                      │
                      ▼
             LangGraph Workflow
          ├── Summary Agent
          ├── Clause Extraction Agent
          ├── Risk Analysis Agent
          └── Conversational AI Agent
                      │
                      ▼
            AI Generated Insights
```

---

# 🛠️ Tech Stack

## Frontend

- Streamlit

## Backend

- Python

## AI & LLM

- OpenAI GPT
- LangChain
- LangGraph

## Retrieval

- FAISS
- OpenAI Embeddings

## Document Processing

- PyMuPDF
- Tesseract OCR
- pdf2image

## Utilities

- NumPy
- Pillow

---

# 📂 Project Structure

```
legal-document-analyzer/

│── backend/
│   ├── agent.py
│   ├── chunking.py
│   ├── document_processor.py
│   ├── file_handler.py
│   ├── ocr.py
│   ├── parser.py
│   ├── rag.py
│   ├── vector_store.py
│   └── workflow.py

│── frontend/
│   └── components/

│── uploads/

│── tests/

│── app.py

│── requirements.txt

│── README.md
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/legal-document-analyzer.git

cd legal-document-analyzer
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure OpenAI API Key

Create a `.env` file

```
OPENAI_API_KEY=your_api_key_here
```

---

## Run Application

```bash
streamlit run app.py
```

---

# 🧠 Workflow

The application follows a complete AI document analysis pipeline.

1. Upload Legal PDF
2. Extract embedded text using PyMuPDF
3. Automatically perform OCR if embedded text is unavailable
4. Split document into semantic chunks
5. Generate OpenAI embeddings
6. Store embeddings inside FAISS
7. Execute LangGraph workflow
8. Generate:
   - Summary
   - Clause Extraction
   - Risk Analysis
   - Conversational Responses

---

# 📊 Evaluation

The application was evaluated using both searchable and scanned legal PDF documents.

### Successfully Tested

- ✅ Embedded Text PDFs
- ✅ Scanned PDFs (OCR)
- ✅ Semantic Retrieval
- ✅ AI Summarization
- ✅ Clause Extraction
- ✅ Risk Identification
- ✅ Conversational Question Answering
- ✅ LangGraph Workflow Execution

---

# 📷 Application Screenshots

Add screenshots here before submission.

Example:

```
screenshots/

home.png

summary.png

clauses.png

risk.png

chat.png
```

---

# 📈 Future Enhancements

- Support image uploads (JPG, PNG, JPEG)
- Automatic legal document classification
- Named Entity Recognition (NER)
- Multi-language OCR support
- Legal citation generation
- Cloud deployment
- User authentication
- Export AI reports as PDF

---

# 👨‍💻 Author

**Sagarika Pramod**

B.Tech Electronics & Computer Science (AI & ML)

Pillai College of Engineering

---

# 🙏 Acknowledgements

- OpenAI
- LangChain
- LangGraph
- Streamlit
- FAISS
- PyMuPDF
- Tesseract OCR

---

# 📜 License

This project was developed as part of the **Generative AI Internship Capstone Project** for educational purposes.
