from pydantic import BaseModel


class Page(BaseModel):
    page_number: int
    text: str


class Chunk(BaseModel):
    chunk_id: str
    text: str
    source_file: str
    page_number: int
    chunk_index: int