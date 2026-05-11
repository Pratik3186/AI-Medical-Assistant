import os
import time

from pathlib import Path
from dotenv import load_dotenv

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

# all-MiniLM-L6-v2 = 384 dimensions
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

    for file in uploaded_files:

        # -------------------------
        # SAVE FILE
        # -------------------------

        save_path = Path(UPLOAD_DIR) / file.filename

        with open(save_path, "wb") as f:
            f.write(file.file.read())

        # -------------------------
        # LOAD PDF
        # -------------------------

        loader = PyPDFLoader(str(save_path))

        documents = loader.load()

        # -------------------------
        # SPLIT DOCUMENTS
        # -------------------------

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=200,
            chunk_overlap=20
        )

        chunks = splitter.split_documents(documents)

        # LIMIT chunks for Railway free tier
        chunks = chunks[:5]

        texts = [
            chunk.page_content
            for chunk in chunks
        ]

        # -------------------------
        # CREATE METADATA
        # -------------------------

        metadatas = []

        for chunk in chunks:

            metadatas.append({
                "source": str(save_path),
                "text": chunk.page_content[:1000]
            })

        # -------------------------
        # IDS
        # -------------------------

        ids = [
            f"{Path(file.filename).stem}-{i}"
            for i in range(len(chunks))
        ]

        # -------------------------
        # EMBEDDINGS
        # -------------------------

        print("Generating embeddings...")

        embeddings = embed_model.embed_documents(texts)

        print("Embeddings generated successfully")

        # -------------------------
        # UPSERT TO PINECONE
        # -------------------------

        vectors = []

        for i in range(len(ids)):

            vectors.append((
                ids[i],
                embeddings[i],
                metadatas[i]
            ))

        # Upload in batches
        batch_size = 5

        for i in range(0, len(vectors), batch_size):

            batch = vectors[i:i + batch_size]

            print("Uploading batch to Pinecone...")

            index.upsert(vectors=batch)

            print("Batch uploaded")

        print(f"Upload complete: {file.filename}")