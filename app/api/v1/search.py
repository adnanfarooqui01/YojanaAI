from fastapi import APIRouter

from app.models.search import SearchRequest, SearchResponse
from app.services.retrieval import retrieve

router = APIRouter(tags=["Search"])


@router.post("/search", response_model=SearchResponse)
def search_chunks(request: SearchRequest) -> SearchResponse:
    return SearchResponse(query=request.query, hits=retrieve(request.query, request.top_k))
    