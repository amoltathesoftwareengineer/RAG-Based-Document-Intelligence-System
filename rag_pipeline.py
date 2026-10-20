
from embeddings import create_embeddings
from vector_store import build_vector_store, search_vector_store


def build_rag_index(chunks):
    """Create a searchable index from document chunks."""
    if not chunks:
        raise ValueError("At least one text chunk is required.")

    embeddings = create_embeddings(chunks)
    index = build_vector_store(embeddings, chunks)

    return index, chunks


def retrieve_context(question, index, chunks, top_k=3):
    """Retrieve document passages relevant to a question."""
    if not isinstance(question, str) or not question.strip():
        raise ValueError("Question must not be empty.")

    query_embedding = create_embeddings([question])[0]

    results = search_vector_store(
        index=index,
        query_embedding=query_embedding,
        chunks=chunks,
        top_k=top_k,
    )

    return {
        "question": question,
        "context": [item["text"] for item in results],
        "sources": results,
    }
