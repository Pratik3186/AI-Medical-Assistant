# server/modules/load_vectorstore.py

import os
import time

from pathlib import Path
from dotenv import load_dotenv
from tqdm.auto import tqdm

from pinecone import Pinecone, ServerlessSpec

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings


load_dotenv()

# =========================
# ENV VARIABLES
# =========================

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")
if not PINECONE_INDEX_NAME:
    raise ValueError("PINECONE_INDEX_NAME is missing")

PINECONE_ENV = "us-east-1"

# =========================
# UPLOAD DIRECTORY
# =========================

UPLOAD_DIR = "uploaded_docs"

os.makedirs(UPLOAD_DIR, exist_ok=True)

# =========================
# PINECONE SETUP
# =========================

pc = Pinecone(api_key=PINECONE_API_KEY)

existing_indexes = [
    index["name"]
    for index in pc.list_indexes()
]

# HuggingFace all-MiniLM-L6-v2 → 384 dimensions
if PINECONE_INDEX_NAME not in existing_indexes:

    pc.create_index(
        name=PINECONE_INDEX_NAME,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region=PINECONE_ENV
        )
    )

    while not pc.describe_index(PINECONE_INDEX_NAME).status["ready"]:
        time.sleep(1)

index = pc.Index(PINECONE_INDEX_NAME)

# =========================
# EMBEDDING MODEL
# =========================

embed_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"}
)

# =========================
# LOAD VECTORSTORE
# =========================


def load_vectorstore(uploaded_files):

    file_paths = []

    # -------------------------
    # SAVE FILES
    # -------------------------

    for file in uploaded_files:

        save_path = Path(UPLOAD_DIR) / file.filename

        with open(save_path, "wb") as f:
            f.write(file.file.read())

        file_paths.append(str(save_path))

    # -------------------------
    # PROCESS FILES
    # -------------------------

    for file_path in file_paths:

        loader = PyPDFLoader(file_path)

        documents = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )

        chunks = splitter.split_documents(documents)

        texts = [
            chunk.page_content
            for chunk in chunks
        ]

        # IMPORTANT
        metadatas = [
            {
                **chunk.metadata,
                "text": chunk.page_content
            }
            for chunk in chunks
        ]

        ids = [
            f"{Path(file_path).stem}-{i}"
            for i in range(len(chunks))
        ]

        print(f"Embedding {len(texts)} chunks...")

        embeddings = embed_model.embed_documents(texts)

        vectors = list(
            zip(ids, embeddings, metadatas)
        )

        print("Uploading to Pinecone...")

        with tqdm(
            total=len(vectors),
            desc="Upserting to Pinecone"
        ) as progress:

            index.upsert(vectors=vectors)

            progress.update(len(vectors))

        print(f"Upload complete for {file_path}")