import streamlit as st


def render_history_download():

    st.subheader("~ Chat History")

    if "messages" in st.session_state:

        history_text = ""

        for msg in st.session_state.messages:
            history_text += f'{msg["role"].upper()}: {msg["content"]}\n\n'

        st.download_button(
            label="⬇ Download Chat History",
            data=history_text,
            file_name="medical_chat_history.txt",
            mime="text/plain"
        )