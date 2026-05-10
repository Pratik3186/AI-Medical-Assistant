import streamlit as st
import requests

BACKEND_URL = "https://ai-medical-assistant-1-ut3l.onrender.com/ask/"


def render_chat():

    st.subheader("~ Chat With Medical Assistant")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_input = st.chat_input("Ask your medical question...")

    if user_input:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": user_input
            }
        )

        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):

            with st.spinner("Analyzing medical documents..."):

                try:

                    response = requests.post(
                        BACKEND_URL,
                        data={"question": user_input},
                        timeout=300
                    )

                    if response.status_code == 200:

                        result = response.json()

                        answer = result.get(
                            "response",
                            "No response generated"
                        )

                        st.markdown(answer)

                        st.session_state.messages.append(
                            {
                                "role": "assistant",
                                "content": answer
                            }
                        )

                    else:
                        st.error("Backend Error ❌")

                except Exception as e:
                    st.error(f"Connection Error: {e}")