import streamlit as st


def render_pipeline(current_stage="Ready"):
    stages = [
        ("📤", "Upload"),
        ("📄", "Extract"),
        ("🔍", "OCR"),
        ("✂️", "Chunk"),
        ("🧠", "Embeddings"),
        ("🗂️", "FAISS"),
        ("⚖️", "Analysis")
    ]

    st.markdown("###  Processing Pipeline")

    cols = st.columns(len(stages))

    reached_current = False

    for i, (icon, label) in enumerate(stages):

        if label == current_stage:
            reached_current = True

        if reached_current:
            bg = "#1E293B"
            border = "#334155"
        else:
            bg = "#1D4ED8"
            border = "#3B82F6"

        with cols[i]:
            st.markdown(
                f"""
                <div style="
                    background:{bg};
                    border:1px solid {border};
                    border-radius:16px;
                    padding:10px;
                    text-align:center;
                    min-height:70px;
                ">
                    <div style="font-size:22px;">{icon}</div>
                    <div style="
                        color:white;
                        margin-top:8px;
                        font-weight:600;
                    ">
                        {label}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)