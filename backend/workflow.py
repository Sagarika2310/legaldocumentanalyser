from typing import TypedDict, Optional, Any

from langgraph.graph import StateGraph, START, END

from backend.document_processor import DocumentProcessor
from backend.chunking import DocumentChunker
from backend.vector_store import VectorStore
from backend.rag import RAGEngine
from backend.agent import LegalAgent


# ==========================================================
# Workflow State
# ==========================================================

class WorkflowState(TypedDict):
    file_path: str

    text: str
    metadata: dict

    chunks: list

    vector_store: Any
    rag_engine: Any
    legal_agent: Any

    status: str
    error: Optional[str]


# ==========================================================
# Agent 1
# Document Processing Agent
# ==========================================================

def document_processing_agent(state: WorkflowState):

    try:

        processor = DocumentProcessor()

        result = processor.process_document(
            state["file_path"]
        )

        state["text"] = result["text"]
        state["metadata"] = result["metadata"]

        state["status"] = "Document Processed"

        return state

    except Exception as e:

        state["error"] = str(e)
        state["status"] = "Failed"

        return state


# ==========================================================
# Agent 2
# Knowledge Preparation Agent
# ==========================================================

def knowledge_agent(state: WorkflowState):

    try:

        chunker = DocumentChunker()

        chunks = chunker.split_text(
            state["text"]
        )

        vector_store = VectorStore()

        vector_store.create_vector_store(
            chunks
        )

        rag = RAGEngine(
            vector_store
        )

        state["chunks"] = chunks
        state["vector_store"] = vector_store
        state["rag_engine"] = rag

        state["status"] = "Knowledge Ready"

        return state

    except Exception as e:

        state["error"] = str(e)
        state["status"] = "Failed"

        return state


# ==========================================================
# Agent 3
# Legal Review Agent
# ==========================================================

def legal_review_agent(state: WorkflowState):

    try:

        agent = LegalAgent(
            state["rag_engine"]
        )

        state["legal_agent"] = agent

        state["status"] = "Legal Agent Ready"

        return state

    except Exception as e:

        state["error"] = str(e)
        state["status"] = "Failed"

        return state


# ==========================================================
# Build Graph
# ==========================================================

graph = StateGraph(WorkflowState)

graph.add_node(
    "document_processing",
    document_processing_agent
)

graph.add_node(
    "knowledge",
    knowledge_agent
)

graph.add_node(
    "legal_review",
    legal_review_agent
)

graph.add_edge(
    START,
    "document_processing"
)

graph.add_edge(
    "document_processing",
    "knowledge"
)

graph.add_edge(
    "knowledge",
    "legal_review"
)

graph.add_edge(
    "legal_review",
    END
)

workflow = graph.compile()


# ==========================================================
# Helper
# ==========================================================

def initialize_workflow(file_path: str):

    initial_state = {

        "file_path": file_path,

        "text": "",

        "metadata": {},

        "chunks": [],

        "vector_store": None,

        "rag_engine": None,

        "legal_agent": None,

        "status": "Starting",

        "error": None,
    }

    return workflow.invoke(initial_state)