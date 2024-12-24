# PDF-Driven Chatbot

This project implements a **PDF-Driven Chatbot** built using **Streamlit**, **LangChain**, and **Google Generative AI APIs**. The chatbot extracts text from uploaded PDF documents, processes it into retrievable chunks, and provides context-aware responses to user queries.

---

## ✨ Features
- **PDF Parsing**: Extracts text content from user-uploaded PDF files.
- **Text Chunking**: Splits extracted text into manageable chunks with overlap for context retention.
- **Semantic Embeddings**: Generates embeddings using Google Generative AI embeddings.
- **FAISS Integration**: Efficient similarity search for text retrieval.
- **Conversational Memory**: Maintains chat context using LangChain's memory module.
- **Interactive UI**: Built with Streamlit for a seamless experience.

---

## 🛠️ Tech Stack
- **Streamlit**: For building the user interface.
- **PyPDF2**: For PDF text extraction.
- **LangChain**: Utilities for text processing and conversational chains.
- **FAISS**: Scalable vector storage and similarity search.
- **Google Generative AI**:
  - `GoogleGenerativeAIEmbeddings` for embedding generation.
  - `ChatGoogleGenerativeAI` for generating conversational responses.

---

## 🚀 How It Works
1. **Upload PDFs**: Users upload PDF documents through the sidebar.
2. **Process PDFs**:
   - Text is extracted and split into chunks.
   - Chunks are embedded using Google Generative AI embeddings.
   - A FAISS vector store is created for efficient retrieval.
3. **Interactive Chat**:
   - Users can ask questions about the content of the uploaded PDFs.
   - The chatbot retrieves relevant information and provides contextually aware responses.

---

## 🖥️ Setup Instructions
### Prerequisites
- Python 3.7+
- A Google Cloud API key with access to Generative AI services.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/pdf-driven-chatbot.git
   cd pdf-driven-chatbot
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add your Google API Key in .streamlit/secrets.toml file:
   ```bash
   GOOGLE_API_KEY = "your-google-api-key"
   ```

## Running the App
Start the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## ⚙️ Usage
1. **Upload PDFs**: Use the file uploader in the sidebar to add your PDF documents.
   
![Screenshot 2024-12-24 191900](https://github.com/user-attachments/assets/42af675c-a7a4-4003-a881-ae38e0db50d7)

2. **Process PDFs**: Click "Process" to analyze the documents and create the vector store.
   
![Screenshot 2024-12-24 191933](https://github.com/user-attachments/assets/25bd89a3-ffdd-47b1-8a9b-81db8d4ce551)

3. **Ask Questions**: Type your question in the input box, and the chatbot will respond with information from the uploaded PDFs.

![Screenshot 2024-12-24 192006](https://github.com/user-attachments/assets/852fc7b6-6f66-42f6-9a62-3a8861b0d023)

![Screenshot 2024-12-24 192055](https://github.com/user-attachments/assets/8fcfaf89-fe37-4a55-8357-bc61d52b1a21)


## 🛡️ Acknowledgments
- [LangChain](https://python.langchain.com/docs/introduction/)
- [Streamlit](https://streamlit.io/)
- [Google Generative AI](https://ai.google.dev/)



