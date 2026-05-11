# 🩺 AI Medical Assistant

> **An AI-powered Medical RAG Assistant that allows users to upload medical PDFs, build vector embeddings, and ask intelligent health-related questions using LLMs + Pinecone.**

---

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-red?style=for-the-badge&logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-RAG-purple?style=for-the-badge)
![Pinecone](https://img.shields.io/badge/Pinecone-VectorDB-black?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-Llama3-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-Apache_2.0-yellow?style=for-the-badge)

---

# 🚀 Live Demo

## 🌐 Streamlit Frontend

👉 https://ai-medical-assistant-bedsfzaashxjj8qqb9ujj.streamlit.app/

---

# 📸 Demo Screenshot

<img width="1873" height="971" alt="Screenshot from 2026-05-11 13-30-09" src="https://github.com/user-attachments/assets/0c39aa46-c0fb-4a50-8d9f-a19a417e3e83" />


---

# 📖 Project Overview

AI Medical Assistant is a **Retrieval-Augmented Generation (RAG)** based healthcare assistant that allows users to upload medical PDF documents and ask contextual questions from them.

The system processes uploaded PDFs, generates semantic embeddings, stores them inside **Pinecone Vector Database**, and retrieves relevant chunks to generate intelligent medical responses using **Groq Llama 3**.

This project was built to explore:

- Medical AI systems
- RAG pipelines
- Vector databases
- FastAPI backend development
- Streamlit frontend integration
- LLM-powered document understanding

---

# 🧠 Features

✅ Upload Medical PDFs  
✅ AI Medical Question Answering  
✅ Semantic Search using Pinecone  
✅ HuggingFace Embeddings  
✅ Groq Llama 3 Integration  
✅ Retrieval-Augmented Generation (RAG)  
✅ FastAPI Backend APIs  
✅ Streamlit Interactive UI  
✅ PDF Chunking & Embeddings  
✅ Chat History Export  
✅ Railway + Streamlit Deployment Ready  

---

# 🏗️ System Architecture

```text
                ┌─────────────────────┐
                │  Streamlit Frontend │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │   FastAPI Backend   │
                └──────────┬──────────┘
                           │
            ┌──────────────┴──────────────┐
            ▼                             ▼
   ┌────────────────┐           ┌─────────────────┐
   │ PDF Processing │           │ User Questions  │
   └────────────────┘           └─────────────────┘
            │                             │
            ▼                             ▼
 ┌────────────────────┐       ┌────────────────────┐
 │ Text Chunking      │       │ Similarity Search  │
 └────────────────────┘       └────────────────────┘
            │                             │
            ▼                             ▼
 ┌────────────────────┐       ┌────────────────────┐
 │ HuggingFace        │       │ Pinecone Vector DB │
 │ Embeddings         │       └────────────────────┘
 └────────────────────┘                  │
            │                             ▼
            └──────────────► Retrieved Context
                                          │
                                          ▼
                               ┌─────────────────┐
                               │ Groq Llama 3    │
                               │ Response Gen    │
                               └─────────────────┘
```

---

# ⚡ Tech Stack

## 🖥️ Frontend

- Streamlit
- Custom CSS
- Interactive Chat UI

## ⚙️ Backend

- FastAPI
- Uvicorn
- Python

## 🤖 AI / RAG

- LangChain
- HuggingFace Embeddings
- Groq Llama 3
- Pinecone Vector Database

## 📄 Document Processing

- PyPDFLoader
- RecursiveCharacterTextSplitter

---

# 📂 Project Structure

```bash
AI-Medical-Assistant/
│
├── client/
│   ├── components/
│   │   ├── upload.py
│   │   ├── chatUI.py
│   │   └── history_download.py
│   │
│   ├── app.py
│   └── config.py
│
├── server/
│   ├── middlewares/
│   ├── modules/
│   │   ├── routes/
│   │   │   ├── upload_pdf.py
│   │   │   └── ask_question.py
│   │   │
│   │   ├── load_vectorstore.py
│   │   ├── query_handlers.py
│   │   ├── pdf_handlers.py
│   │   └── llm.py
│   │
│   ├── logger.py
│   └── main.py
│
├── uploaded_docs/
├── requirements.txt
├── README.md
└── .env
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/Pratik3186/AI-Medical-Assistant.git

cd AI-Medical-Assistant
```

---

## 2️⃣ Create Virtual Environment

### Linux / Mac

```bash
python3 -m venv .venv

source .venv/bin/activate
```

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Create `.env` File

```env
GOOGLE_API_KEY=your_google_api_key

GROQ_API_KEY=your_groq_api_key

PINECONE_API_KEY=your_pinecone_api_key

PINECONE_INDEX_NAME=medicalindex
```

---

# ▶️ Run Backend

```bash
uvicorn server.main:app --reload
```

Backend runs on:

```bash
http://127.0.0.1:8000
```

---

# ▶️ Run Frontend

```bash
streamlit run client/app.py
```

Frontend runs on:

```bash
http://localhost:8501
```

---

# 🧬 Embedding & Chunking Strategy

## 🔹 Embedding Model

```python
sentence-transformers/all-MiniLM-L6-v2
```

- Lightweight
- Fast inference
- 384-dimensional embeddings

---

## 🔹 Chunking Strategy

```python
chunk_size = 500
chunk_overlap = 50
```

This improves:

- Retrieval quality
- Semantic understanding
- Context continuity

---

# 🧠 How It Works

1. User uploads medical PDFs  
2. PDFs are processed and chunked  
3. HuggingFace creates embeddings  
4. Embeddings are stored in Pinecone  
5. User asks medical questions  
6. Relevant chunks are retrieved  
7. Groq Llama 3 generates contextual responses  

---

# 📈 Future Improvements

- [ ] Multi-user authentication
- [ ] OCR support
- [ ] Voice assistant integration
- [ ] Medical image analysis
- [ ] Docker deployment
- [ ] Kubernetes scaling
- [ ] Multi-document chat memory

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

---

# 📜 License

Licensed under the Apache 2.0 License.

---

# 👨‍💻 Built By

## Pratik

🎓 Computer Science Engineer  
🧠 AI + Medical AI Enthusiast  
🌐 Full Stack Developer  

### 🔗 Connect With Me

- GitHub: https://github.com/Pratik3186
- LinkedIn: https://www.linkedin.com/in/pratik-kumar-50321a21b/
- Leetcode: https://leetcode.com/u/Prratikkkkk/

---

# ⭐ Support

If you found this project useful:

⭐ Star this repository  
🍴 Fork the project  
📢 Share with others

---

# 🩺 Disclaimer

> This project is intended for educational and research purposes only and should not replace professional medical advice.
