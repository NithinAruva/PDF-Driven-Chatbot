import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import faiss

VECTORSTORE_FILE = "vectorstore.index"  

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def load_vectorstore():
    if os.path.exists(VECTORSTORE_FILE):
        index = faiss.read_index(VECTORSTORE_FILE)
        return FAISS(index)
    return None

def save_vectorstore(vectorstore):
    faiss.write_index(vectorstore.index, VECTORSTORE_FILE)

def get_conversation_chain(vectorstore):
    llm = ChatGoogleGenerativeAI(google_api_key=st.secrets["GOOGLE_API_KEY"], model="gemini-1.5-pro")
    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history.append({"user": user_question, "bot": response['chat_history'][-1].content})

def display_chat_history():
    for chat in st.session_state.chat_history:
        st.write(user_template.replace("{{MSG}}", chat["user"]), unsafe_allow_html=True)
        st.write(bot_template.replace("{{MSG}}", chat["bot"]), unsafe_allow_html=True)

def main():
    st.title("PDF Driven ChatBot")
    st.write(css, unsafe_allow_html=True)
    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader("Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
        if st.button("Process") and pdf_docs:
            with st.spinner("Processing"):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                vectorstore = get_vectorstore(text_chunks)
                save_vectorstore(vectorstore)
                st.session_state.vectorstore = vectorstore
                st.session_state.conversation = get_conversation_chain(vectorstore)
                st.session_state.chat_history = []

    if "conversation" not in st.session_state:
        vectorstore = load_vectorstore()
        if vectorstore:
            st.session_state.vectorstore = vectorstore
            st.session_state.conversation = get_conversation_chain(vectorstore)
            st.session_state.chat_history = []

    if "chat_history" in st.session_state:
        display_chat_history()

    user_question = st.text_input("Ask me a question?")

    if user_question:
        if not st.session_state.get('last_question') == user_question:
            handle_userinput(user_question)
            st.session_state['last_question'] = user_question
            st.rerun()

if __name__ == '__main__':
    main()
