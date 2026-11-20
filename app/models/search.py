from pydantic import BaseModel, Field


class SearchRequest(BaseModel):
    query: str = Field(min_length=3, max_length=500)
    top_k: int = Field(default=5, ge=1, le=20)


class SearchHit(BaseModel):
    score: float
    source_file: str
    page_number: int
    text: str


class SearchResponse(BaseModel):
    query: str
    hits: list[SearchHit]