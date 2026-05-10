
import streamlit as st
from components.upload import render_uploader
from components.history_download import render_history_download
from components.chatUI import render_chat

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="AI Medical Assistant",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown(
    """
    <style>

    /* =========================
       MAIN APP
    ========================== */
    .stApp {
        background: linear-gradient(to right, #f8f8f7, #efefec);
        color: #1f2937;
        font-family: 'Inter', sans-serif;
    }

    /* =========================
       HEADER
    ========================== */
    .main-title {
        font-size: 3.2rem;
        font-weight: 800;
        color: #111827;
        text-align: center;
        margin-bottom: 0.4rem;
        letter-spacing: -1px;
    }

    .sub-title {
        text-align: center;
        color: #6b7280;
        font-size: 1.08rem;
        margin-bottom: 2rem;
    }

    /* =========================
       GLASS CARDS
    ========================== */
    .glass-card {
        background: #fcfcfb;
        padding: 1.5rem;
        border-radius: 24px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.05);
        border: 1px solid #e5e7eb;
        margin-bottom: 1.2rem;
    }

    /* =========================
       METRIC CARDS
    ========================== */
    .metric-card {
        background: #ffffff;
        padding: 1.2rem;
        border-radius: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.04);
        text-align: center;
        border: 1px solid #ececec;
        transition: 0.3s ease;
    }

    .metric-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 18px rgba(0,0,0,0.06);
    }

    .metric-title {
        font-size: 0.95rem;
        color: #6b7280;
        margin-bottom: 0.3rem;
    }

    .metric-value {
        font-size: 1.45rem;
        font-weight: 700;
        color: #374151;
    }

    /* =========================
       FILE UPLOADER
    ========================== */
    section[data-testid="stFileUploader"] {
        background: #f3f4f6;
        border: 2px dashed #9ca3af;
        padding: 1.5rem;
        border-radius: 18px;
    }

    div[data-testid="stFileUploader"] button {
        background: #111827 !important;
        color: white !important;
        border-radius: 14px !important;
        font-weight: 600 !important;
        padding: 0.65rem 1.2rem !important;
        border: none !important;
        transition: all 0.3s ease;
    }

    div[data-testid="stFileUploader"] button:hover {
        background: #374151 !important;
        transform: scale(1.02);
    }

    /* =========================
       NORMAL BUTTONS
    ========================== */
    .stButton > button {
        background: #111827;
        color: white;
        border-radius: 14px;
        border: none;
        padding: 0.7rem 1.2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        background: #374151;
        transform: translateY(-2px);
    }

    /* =========================
       CHAT INPUT
    ========================== */
    .stChatInputContainer {
        border-radius: 16px !important;
        border: 1px solid #d1d5db !important;
        background: white !important;
    }

    /* =========================
       SIDEBAR
    ========================== */
    section[data-testid="stSidebar"] {
        background: #f5f5f4;
        border-right: 1px solid #e5e7eb;
    }

    /* SIDEBAR TEXT */
    section[data-testid="stSidebar"] * {
        color: #1f2937 !important;
    }

    /* SIDEBAR HEADINGS */
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #111827 !important;
        font-weight: 700;
    }

    /* SIDEBAR LIST ITEMS */
    section[data-testid="stSidebar"] li {
        color: #374151 !important;
        margin-bottom: 0.35rem;
    }

    /* REMOVE WEIRD GREY BACKGROUND */
    section[data-testid="stSidebar"] div,
    section[data-testid="stSidebar"] span {
        background: transparent !important;
    }

    /* =========================
       INFO BOX
    ========================== */
    div[data-baseweb="notification"] {
        background: #e7eef7 !important;
        border: 1px solid #c7d7ea !important;
        border-radius: 16px !important;
        color: #1e3a5f !important;
    }

    div[data-baseweb="notification"] p {
        color: #1e3a5f !important;
        font-weight: 500;
        line-height: 1.6;
    }

    /* =========================
       SUCCESS BOX
    ========================== */
    div[data-baseweb="notification"][kind="success"] {
        background: #e8f5eb !important;
        border: 1px solid #b9e2c0 !important;
        color: #166534 !important;
    }

    /* =========================
       CHAT MESSAGE STYLING
    ========================== */
    .stChatMessage {
        background: white !important;
        border-radius: 18px !important;
        padding: 0.8rem !important;
        border: 1px solid #ececec !important;
    }

    /* =========================
       INPUT BOXES
    ========================== */
    .stTextInput > div > div > input {
        border-radius: 14px;
        border: 1px solid #d1d5db;
        padding: 0.7rem;
    }

    /* =========================
       FOOTER
    ========================== */
    .footer {
        text-align: center;
        color: #6b7280;
        margin-top: 2rem;
        padding: 1rem;
        font-size: 0.95rem;
    }

    <style>

    /* USER CHAT MESSAGE */
    div[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-user"]) {
        background: #ffffff !important;
        border: 1px solid #dbe4ee !important;
        border-radius: 18px !important;
        padding: 1rem !important;
        color: #111827 !important;
    }

    /* BOT CHAT MESSAGE */
    div[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-assistant"]) {
        background: #f8fafc !important;
        border: 1px solid #dbe4ee !important;
        border-radius: 18px !important;
        padding: 1rem !important;
        color: #111827 !important;
    }

    /* FORCE TEXT COLOR */
    div[data-testid="stChatMessage"] p,
    div[data-testid="stChatMessage"] span,
    div[data-testid="stChatMessage"] div {
        color: #111827 !important;
        font-size: 1rem !important;
        line-height: 1.6 !important;
    }

    /* CHAT INPUT */
    .stChatInputContainer textarea {
        color: white !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# HEADER SECTION
# -----------------------------
st.markdown(
    """
    <div class="main-title">AI Medical Assistant</div>
    <div class="sub-title">
        Upload medical documents, ask intelligent health-related questions,
        and get AI-powered contextual answers.
    </div>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# METRICS SECTION
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-title">AI Model</div>
            <div class="metric-value">Groq Llama 3</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-title">Vector Database</div>
            <div class="metric-value">Pinecone</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="metric-card">
            <div class="metric-title">Embeddings</div>
            <div class="metric-value">HuggingFace</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:

    st.markdown("## Assistant Settings")

    st.info(
        "This assistant uses Retrieval-Augmented Generation (RAG) to answer questions from uploaded medical PDFs."
    )

    st.markdown("---")

    st.markdown("### AI Capabilities")
    st.markdown(
        """
        - PDF Understanding
        - Medical Question Answering
        - Context-Aware Retrieval
        - AI Summarization
        - Semantic Search
        """
    )

    st.markdown("---")

    st.success("System Running")

# -----------------------------
# MAIN CONTENT
# -----------------------------
left_col, right_col = st.columns([1, 2])

# LEFT PANEL
with left_col:

    st.markdown(
        '<div class="glass-card">',
        unsafe_allow_html=True
    )

    st.subheader("~ Upload Medical Documents")

    render_uploader()

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="glass-card">',
        unsafe_allow_html=True
    )

    st.subheader("~ Export Conversation")

    render_history_download()

    st.markdown('</div>', unsafe_allow_html=True)

# RIGHT PANEL
with right_col:

    st.markdown(
        '<div class="glass-card">',
        unsafe_allow_html=True
    )

    st.subheader("~ Medical Chat Assistant")

    render_chat()

    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown(
    """
    <div class="footer">
        Built with ❤️ using FastAPI, LangChain, Pinecone, Groq, and Streamlit.
    </div>
    """,
    unsafe_allow_html=True
)


