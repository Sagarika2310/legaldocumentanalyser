"""
LexiScan AI
Main Application
"""

import streamlit as st

from backend.file_handler import save_uploaded_file
from backend.workflow import initialize_workflow

from frontend.components.hero import render_hero
from frontend.components.pipeline import render_pipeline
from frontend.components.upload_card import render_upload_card
from frontend.components.health_card import render_health_card
from frontend.components.chat_panel import render_chat_panel



# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="LexiScan AI",
    page_icon="⚖️",
    layout="wide"
)


# =====================================================
# SESSION STATE
# =====================================================

defaults = {
    "agent": None,
    "metadata": None,
    "processed": False,
    "chunk_count": 0,
    "messages": [
        {
            "role": "assistant",
            "content": "👋 Welcome to LexiScan AI! Upload a legal document to begin."
        }
    ]
}

for key, value in defaults.items():

    if key not in st.session_state:

        st.session_state[key] = value


# =====================================================
# GLOBAL CSS
# =====================================================

st.markdown("""
<style>

.stApp{
    background:#0B1120;
}

.block-container{
    padding-top:1.4rem;
    max-width:1500px;
}

section[data-testid="stSidebar"]{
    display:none;
}

footer{
    visibility:hidden;
}

header{
    visibility:hidden;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# HERO
# =====================================================

render_hero()


# =====================================================
# PIPELINE
# =====================================================

render_pipeline()


# =====================================================
# UPLOAD SECTION
# =====================================================

uploaded = render_upload_card()


# =====================================================
# DOCUMENT PROCESSING
# =====================================================

if uploaded:

    with st.spinner("Preparing your legal workspace..."):

        file_path = save_uploaded_file(uploaded)

        workflow_state = initialize_workflow(file_path)

        if workflow_state["error"]:

            st.error(workflow_state["error"])

        else:

            st.session_state.agent = workflow_state["legal_agent"]

            st.session_state.metadata = workflow_state["metadata"]

            st.session_state.chunk_count = len(
                workflow_state["chunks"]
            )

            st.session_state.processed = True

            st.success(
                "✅ Document processed successfully."
            )


# =====================================================
# MAIN WORKSPACE
# =====================================================

health_col, workspace_col = st.columns(
    [1,2],
    gap="large"
)

# =====================================================
# DOCUMENT HEALTH CARD
# =====================================================

with health_col:

    render_health_card(
        st.session_state.metadata,
        st.session_state.chunk_count
    )


# =====================================================
# AI WORKSPACE
# =====================================================

with workspace_col:

    render_chat_panel(
        st.session_state.agent
    )




# =====================================================
# FOOTER
# =====================================================

st.divider()

st.caption(
    "⚖️ LexiScan AI • Powered by LangGraph • OpenAI • FAISS • PyMuPDF • Streamlit"
)
