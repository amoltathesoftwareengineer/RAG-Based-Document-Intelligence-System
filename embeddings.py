
from sentence_transformers import SentenceTransformer


MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


def create_embeddings(texts):
    """Convert text chunks into normalized vector embeddings."""
    if not texts:
        return []

    if not all(isinstance(text, str) and text.strip() for text in texts):
        raise ValueError("All texts must be non-empty strings.")

    model = SentenceTransformer(MODEL_NAME)

    embeddings = model.encode(
        texts,
        normalize_embeddings=True,
        convert_to_numpy=True,
    )

    return embeddings
