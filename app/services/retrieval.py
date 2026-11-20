from app.models.search import SearchHit
from app.rag.embedder import embed_query
from app.rag.vector_store import search


def retrieve(query: str, top_k: int = 5) -> list[SearchHit]:
    points = search(embed_query(query), limit=top_k)
    return [
        SearchHit(
            score=p.score,
            source_file=p.payload["source_file"],
            page_number=p.payload["page_number"],
            text=p.payload["text"],
        )
        for p in points
    ]