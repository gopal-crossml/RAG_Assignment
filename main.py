import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.runnables import RunnablePassthrough
from cred import gemini_api_key
from constant import (
    MODEL,
    EMBEDDING_MODEL,
    CHUNK_SIZE,
    CHUNK_OVERLAP,
    TOP_K,
    TEMP_PDF_PATH
)
from prompt import RAG_PROMPT
# --------------------
# ENV SETUP
# --------------------
os.environ["GOOGLE_API_KEY"] = gemini_api_key
# --------------------
# STREAMLIT UI
# --------------------
st.set_page_config(page_title="RAG PDF Reader", layout="wide")
st.title(":page_facing_up: RAG-based PDF Reader (Gemini + LangChain)")
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])
# --------------------
# MODELS
# --------------------
llm = ChatGoogleGenerativeAI(
    model=MODEL,
    temperature=0.2
)
embeddings = GoogleGenerativeAIEmbeddings(
    model=EMBEDDING_MODEL
)
# --------------------
# FUNCTIONS
# --------------------
def process_pdf(file):
    with open(TEMP_PDF_PATH, "wb") as f:
        f.write(file.getbuffer())
    loader = PyPDFLoader(TEMP_PDF_PATH)
    documents = loader.load()
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )
    chunks = splitter.split_documents(documents)
    vectorstore = FAISS.from_documents(chunks, embeddings)
    return vectorstore.as_retriever(search_kwargs={"k": TOP_K})
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)
# --------------------
# APP FLOW
# --------------------
if uploaded_file:
    with st.spinner("Processing PDF and building vector store..."):
        retriever = process_pdf(uploaded_file)
    st.success("PDF indexed successfully!")
    question = st.text_input("Ask a question from your PDF")
    if question:
        rag_chain = (
            {
                "context": retriever | format_docs,
                "question": RunnablePassthrough(),
            }
            | RAG_PROMPT
            | llm
        )
        response = rag_chain.invoke(question)
        st.subheader("Answer")
        st.write(response.content)