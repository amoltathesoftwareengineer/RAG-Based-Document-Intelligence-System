
import faiss
import numpy as np


def build_vector_store(embeddings, chunks):
    """Build a FAISS index for text chunks."""
    vectors = np.asarray(embeddings, dtype=np.float32)

    if vectors.ndim != 2 or vectors.shape[0] == 0:
        raise ValueError("Embeddings must be a non-empty 2D array.")

    if len(chunks) != vectors.shape[0]:
        raise ValueError("Each embedding must match one text chunk.")

    if not np.isfinite(vectors).all():
        raise ValueError("Embeddings must contain finite values.")

    faiss.normalize_L2(vectors)

    index = faiss.IndexFlatIP(vectors.shape[1])
    index.add(vectors)

    return index


def search_vector_store(index, query_embedding, chunks, top_k=3):
    """Retrieve the most relevant text chunks for a query embedding."""
    if top_k <= 0:
        raise ValueError("top_k must be greater than zero.")

    if index.ntotal != len(chunks):
        raise ValueError("Index size must match the number of chunks.")

    query = np.asarray(query_embedding, dtype=np.float32)

    if query.ndim == 1:
        query = query.reshape(1, -1)

    if query.ndim != 2 or query.shape[0] != 1:
        raise ValueError("Provide exactly one query embedding.")

    if query.shape[1] != index.d:
        raise ValueError("Query embedding dimension does not match the index.")

    if not np.isfinite(query).all():
        raise ValueError("Query embedding must contain finite values.")

    faiss.normalize_L2(query)

    scores, indices = index.search(query, min(top_k, len(chunks)))

    results = []

    for score, idx in zip(scores[0], indices[0]):
        if idx >= 0:
            results.append({
                "text": chunks[int(idx)],
                "score": float(score),
            })

    return results
