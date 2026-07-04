import streamlit as st


def render_health_card(metadata=None, chunk_count=0):
    st.subheader("📊 Document Health")

    if metadata is None:
        st.info("Upload a legal document to view its health and analysis metrics.")
        return

    # -----------------------------------------
    # Overall Score Calculation
    # -----------------------------------------

    score = 100

    if metadata.get("ocr_used"):
        score -= 5

    if metadata.get("word_count", 0) < 500:
        score -= 10

    if chunk_count < 5:
        score -= 10

    score = max(0, min(score, 100))

    if score >= 90:
        status = "🟢 Excellent"
    elif score >= 75:
        status = "🟡 Good"
    elif score >= 60:
        status = "🟠 Fair"
    else:
        status = "🔴 Needs Review"

    # -----------------------------------------
    # Reading Time
    # -----------------------------------------

    reading_time = max(
        1,
        round(metadata.get("word_count", 0) / 200)
    )

    # -----------------------------------------
    # Overall Score
    # -----------------------------------------

    st.metric(
        label="Overall Score",
        value=f"{score}/100",
        delta=status
    )

    st.success("Ready for Legal Analysis")

    st.divider()

    # -----------------------------------------
    # Document Metrics
    # -----------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "📄 Pages",
            metadata.get("page_count", "-")
        )

        st.metric(
            "📝 Words",
            f"{metadata.get('word_count',0):,}"
        )

        st.metric(
            "📦 Chunks",
            chunk_count
        )

    with col2:

        st.metric(
            "⏱ Reading Time",
            f"{reading_time} min"
        )

        st.metric(
            "🔍 OCR",
            "Enabled" if metadata.get("ocr_used") else "Not Used"
        )

        st.metric(
            "⚡ Processing",
            f"{metadata.get('processing_time',0):.2f} s"
        )

    st.divider()

    st.caption(
        f"📄 {metadata.get('filename', 'Unknown Document')}"
    )