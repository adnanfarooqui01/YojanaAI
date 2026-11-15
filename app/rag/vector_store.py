import uuid
from functools import lru_cache

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams

from app.core.config import get_settings
from app.rag.schemas import Chunk


@lru_cache
def get_client() -> QdrantClient:
    s = get_settings()
    if s.qdrant_url:
        return QdrantClient(url=s.qdrant_url)
    return QdrantClient(path=s.qdrant_path)


def chunk_to_point_id(chunk_id: str) -> str:
    # Qdrant IDs must be integers or UUIDs. uuid5 is deterministic, so the
    # same chunk always gets the same ID and re-indexing overwrites, not duplicates.
    return str(uuid.uuid5(uuid.NAMESPACE_URL, chunk_id))


def ensure_collection() -> None:
    s = get_settings()
    client = get_client()
    if not client.collection_exists(s.qdrant_collection):
        client.create_collection(
            collection_name=s.qdrant_collection,
            vectors_config=VectorParams(size=s.embedding_dim, distance=Distance.COSINE),
        )


def upsert_chunks(chunks: list[Chunk], vectors: list[list[float]]) -> None:
    points = [
        PointStruct(
            id=chunk_to_point_id(c.chunk_id),
            vector=v,
            payload=c.model_dump(),
        )
        for c, v in zip(chunks, vectors, strict=True)
    ]
    get_client().upsert(collection_name=get_settings().qdrant_collection, points=points)


def search(query_vector: list[float], limit: int = 5):
    return get_client().query_points(
        collection_name=get_settings().qdrant_collection,
        query=query_vector,
        limit=limit,
    ).points