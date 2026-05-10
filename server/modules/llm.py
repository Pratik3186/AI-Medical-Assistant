from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


def get_llm_chain(retriever):

    llm = ChatGroq(
        model="llama-3.3-70b-versatile"
    )

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
You are MediBot, a medical assistant AI.

Context:
{context}

Question:
{question}

Answer:
- Be clear and simple
- Use only context
- If not found, say you don't know
"""
    )

    def format_docs(docs):
        return "\n\n".join([doc.page_content for doc in docs])

    chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain