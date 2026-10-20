# 📚 RAG-Based Document Intelligence System

A Python-based document intelligence application that extracts text from PDF files, creates semantic embeddings, and retrieves relevant passages using FAISS vector similarity search.

## 🚀 Features

- Upload PDF documents through a Streamlit interface
- Extract text from PDF files
- Split document text into overlapping chunks
- Generate semantic embeddings using Sentence Transformers
- Build a FAISS vector search index
- Retrieve relevant document passages for user questions
- Validate invalid, empty, and unsupported PDF inputs
- Automated tests with pytest
- GitHub Actions continuous integration

## 🧰 Technology Stack

- Python 3.12
- Streamlit
- PyPDF
- Sentence Transformers
- FAISS
- NumPy
- pytest
- GitHub Actions

## 🏗️ Architecture

1. Upload a PDF document.
2. Extract readable text.
3. Split text into overlapping chunks.
4. Generate embeddings for the chunks.
5. Build a FAISS vector index.
6. Convert the user's question into an embedding.
7. Retrieve the most relevant passages.

## 📂 Project Structure

```text
RAG-Based-Document-Intelligence-System/
├── .github/
│   └── workflows/
│       └── python-tests.yml
├── tests/
│   └── test_document_processing.py
├── app.py
├── document_loader.py
├── text_splitter.py
├── embeddings.py
├── vector_store.py
├── rag_pipeline.py
├── requirements.txt
├── .env.example
├── .gitignore
├── LICENSE
└── README.md
```

## ⚙️ Getting Started

### Prerequisites

- Python 3.12
- pip
- Internet access for downloading the embedding model on first use

### 1. Clone the repository

```bash
git clone https://github.com/amoltathesoftwareengineer/RAG-Based-Document-Intelligence-System.git
cd RAG-Based-Document-Intelligence-System
```

### 2. Create and activate a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS/Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal, usually `http://localhost:8501`.

## 🧪 Run Tests

```bash
python -m pytest -v
```

GitHub Actions runs the automated tests on pushes and pull requests.

## ⚠️ Current Limitations

- The application retrieves relevant passages; it does not yet generate complete answers with an LLM.
- Scanned PDFs may require OCR.
- The vector index is held in application session state and is not persisted between sessions.
- The current implementation focuses on PDF documents.
- Retrieval quality depends on document quality, chunking, and the embedding model.
- Automated tests currently focus on document processing and input validation.

## 🔮 Future Enhancements

- Integrate an LLM to generate context-aware answers
- Display page-level citations for retrieved passages
- Add persistent vector index storage
- Support DOCX, TXT, and Markdown files
- Add OCR for scanned PDFs
- Expand automated tests for embeddings, retrieval, and the UI
- Add Docker deployment support

## 👨‍💻 Author

**Amol Tathe**

- GitHub: [amoltathesoftwareengineer](https://github.com/amoltathesoftwareengineer)
- LinkedIn: [Amol Tathe](https://linkedin.com/in/amoltathesoftwareengineer)

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
