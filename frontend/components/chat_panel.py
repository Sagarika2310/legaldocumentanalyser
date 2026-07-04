import streamlit as st


def render_chat_panel(agent):
    st.subheader("AI Workspace")

    # -------------------------------
    # Session State
    # -------------------------------

    if "current_view" not in st.session_state:
        st.session_state.current_view = "summary"

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Hello! Upload a legal document and ask me anything about it."
            }
        ]

    # -------------------------------
    # Top Navigation Buttons
    # -------------------------------

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("📄 Summary", use_container_width=True):
            st.session_state.current_view = "summary"

            if agent:
                with st.spinner("Generating summary..."):
                    st.session_state.summary = agent.summarize()

    with col2:
        if st.button("📑 Clauses", use_container_width=True):
            st.session_state.current_view = "clauses"

            if agent:
                with st.spinner("Extracting clauses..."):
                    st.session_state.clauses = agent.clauses()

    with col3:
        if st.button("⚠ Risks", use_container_width=True):
            st.session_state.current_view = "risks"

            if agent:
                with st.spinner("Analyzing risks..."):
                    st.session_state.risks = agent.risks()

    with col4:
        if st.button("💬 Ask LexiScan AI", use_container_width=True):
            st.session_state.current_view = "chat"

    st.divider()

    # -------------------------------
    # Dynamic Workspace
    # -------------------------------

    view = st.session_state.current_view

    if view == "summary":

        st.markdown("### 📄 Summary")

        if "summary" in st.session_state:
            st.write(st.session_state.summary)
        else:
            st.info("Click 'Summary' to generate a summary.")

    elif view == "clauses":

        st.markdown("### 📑 Clauses")

        if "clauses" in st.session_state:
            st.write(st.session_state.clauses)
        else:
            st.info("Click 'Clauses' to extract important clauses.")

    elif view == "risks":

        st.markdown("### ⚠ Risk Analysis")

        if "risks" in st.session_state:
            st.write(st.session_state.risks)
        else:
            st.info("Click 'Risks' to analyze the document.")

    elif view == "chat":

        st.markdown("### 💬 Ask LexiScan AI")

        for message in st.session_state.messages:

            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        prompt = st.chat_input("Ask anything about this legal document...")

        if prompt:

            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": prompt
                }
            )

            with st.chat_message("user"):
                st.markdown(prompt)

            if agent:

                with st.spinner("Thinking..."):
                    reply = agent.chat(prompt)

            else:

                reply = "Please upload a legal document first."

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": reply
                }
            )

            with st.chat_message("assistant"):
                st.markdown(reply)