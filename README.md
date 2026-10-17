
# RAG-Based Document Intelligence System

An AI-powered document intelligence application that helps users search documents, retrieve relevant information, summarize content, and answer questions using Retrieval-Augmented Generation (RAG).

## Overview

The system converts uploaded documents into searchable text chunks, creates vector embeddings, retrieves relevant content for a user's question, and uses a language model to generate context-aware answers.

The goal is to make document analysis faster, more organized, and easier to verify.

## Key Features

- Upload and process PDF documents
- Extract and split text into manageable chunks
- Generate semantic embeddings
- Search relevant document passages using vector similarity
- Ask natural-language questions about uploaded documents
- Generate document summaries
- Display source document references where available
- Provide clear error messages for unsupported or empty documents
- Keep API keys and configuration outside source code

## Technology Stack

- Python
- Streamlit
- LangChain
- Sentence Transformers
- FAISS
- PyPDF
- LLM API or a compatible local language model

## System Architecture

User Uploads Documents  
↓  
Document Text Extraction  
↓  
Text Cleaning and Chunking  
↓  
Embedding Generation  
↓  
FAISS Vector Index  
↓  
Relevant Context Retrieval  
↓  
Language Model  
↓  
Answer with Source References

## Project Structure

```text
RAG-Based-Document-Intelligence/
├── app.py
├── document_loader.py
├── text_splitter.py
├── embeddings.py
├── vector_store.py
├── rag_pipeline.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
├── documents/
└── tests/
```

## Getting Started

### Prerequisites

- Python 3.10 or a compatible supported version
- pip
- An LLM API key or a supported local model, if generation is enabled

### Installation

```bash
git clone https://github.com/amoltathesoftwareengineer/RAG-Based-Document-Intelligence.git
cd RAG-Based-Document-Intelligence
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
streamlit run app.py
```

Open the local URL shown in the terminal, normally:

`http://localhost:8501`

## Configuration

Store optional API credentials in a local `.env` file.

Never commit `.env`, API keys, private documents, or credentials to GitHub.

See `.env.example` for the configuration variables required by the implemented model provider.

## Example Use Cases

- Search company policies and internal manuals
- Understand lengthy PDF reports
- Retrieve information from technical documentation
- Summarize research and business documents
- Explore knowledge bases using natural-language questions

## Testing

Run automated tests, when available, using:

```bash
python -m pytest
```

## Limitations

- Answer quality depends on document extraction, retrieval, and the selected language model.
- Scanned PDFs may require OCR support.
- Large document collections may require additional storage and indexing optimizations.
- AI-generated answers should be verified against their cited sources.

## Future Enhancements

- Support DOCX, TXT, and Markdown files
- Add hybrid keyword and semantic retrieval
- Add document-level access controls
- Implement retrieval evaluation and automated tests
- Add a Docker deployment configuration

## Author

**Amol Tathe**

GitHub: https://github.com/amoltathesoftwareengineer

LinkedIn: https://linkedin.com/in/amol-tathe-softwareengineer/

## License

This project is intended as a software engineering and AI learning project. Add an appropriate open-source license before permitting reuse.
