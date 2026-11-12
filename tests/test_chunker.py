import pytest

from app.rag.chunker import split_text


def test_short_text_is_one_chunk() -> None:
    assert split_text("Hello world", 100, 10) == ["Hello world"]


def test_chunks_respect_size_and_overlap() -> None:
    text = "word " * 500
    chunks = split_text(text, chunk_size=200, overlap=50)

    assert len(chunks) > 1
    assert all(len(chunk) <= 200 for chunk in chunks)


def test_invalid_overlap_raises() -> None:
    with pytest.raises(ValueError):
        split_text("abc", chunk_size=100, overlap=100)
