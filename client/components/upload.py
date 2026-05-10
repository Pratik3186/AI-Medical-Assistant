import streamlit as st
import requests

BACKEND_URL = "https://ai-medical-assistant-1-ut3l.onrender.com/upload/"


def render_uploader():

    st.subheader("~ Upload Medical Documents")

    uploaded_files = st.file_uploader(
        "Upload PDF Files",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:

        if st.button("Upload PDFs"):

            files = [
                (
                    "files",
                    (file.name, file, "application/pdf")
                )
                for file in uploaded_files
            ]

            with st.spinner("Uploading and processing PDFs..."):
                response = requests.post(BACKEND_URL, files=files)

            if response.status_code == 200:
                st.success("PDFs uploaded successfully ✅")
            else:
                st.error("Upload failed ❌")