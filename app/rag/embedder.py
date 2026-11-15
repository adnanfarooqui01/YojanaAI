from functools import lru_cache

from sentence_transformers import SentenceTransformer

from app.core.config import get_settings


@lru_cache
def get_model() -> SentenceTransformer:
    return SentenceTransformer(get_settings().embedding_model)


def embed_passages(texts: list[str], batch_size: int = 32) -> list[list[float]]:
    prefixed = [f"passage: {t}" for t in texts]
    vectors = get_model().encode(
        prefixed, batch_size=batch_size, normalize_embeddings=True, show_progress_bar=True
    )
    return vectors.tolist()


def embed_query(text: str) -> list[float]:
    vector = get_model().encode(f"query: {text}", normalize_embeddings=True)
    return vector.tolist()