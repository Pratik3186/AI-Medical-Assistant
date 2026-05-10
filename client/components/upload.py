import streamlit as st
import requests
from config import API_URL


BACKEND_URL = f"{API_URL}/upload/"


def render_uploader():

    st.subheader("~ Upload Medical Documents")

    uploaded_files = st.file_uploader(
        "Upload PDF Files",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:

        st.success(f"{len(uploaded_files)} file(s) selected")

        if st.button("Upload PDFs"):

            files = []

            for file in uploaded_files:
                files.append(
                    (
                        "files",
                        (
                            file.name,
                            file,
                            "application/pdf"
                        )
                    )
                )

            try:

                with st.spinner("Uploading and processing PDFs..."):

                    response = requests.post(
                        BACKEND_URL,
                        files=files,
                        timeout=300
                    )

                if response.status_code == 200:
                    st.success("PDF uploaded successfully ✅")

                else:
                    st.error(f"Upload Failed: {response.text}")

            except Exception as e:
                st.error(f"Error: {str(e)}")