from pathlib import Path

from app.rag.schemas import Chunk, Page


def split_text(
    text: str, chunk_size: int = 800, overlap: int = 150, min_chars: int = 50
) -> list[str]:
    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")
    if min_chars < 0:
        raise ValueError("min_chars must be non-negative")

    chunks: list[str] = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))

        if end < len(text):
            window = text[start:end]
            cut = max(window.rfind(". "), window.rfind("\n"))
            if cut > chunk_size * 0.5:          # prefer ending at a sentence/paragraph
                end = start + cut + 1
            else:
                space = window.rfind(" ")        # otherwise at least don't cut a word
                if space > 0:
                    end = start + space

        piece = text[start:end].strip()
        if len(piece) >= min_chars:
            chunks.append(piece)
        if end >= len(text):
            break
        start = max(end - overlap, start + 1)    # step back by `overlap`, always move forward

    return chunks


def chunk_pages(
    pages: list[Page], source_file: str, chunk_size: int, overlap: int
) -> list[Chunk]:
    stem = Path(source_file).stem
    result: list[Chunk] = []
    for page in pages:
        for index, piece in enumerate(split_text(page.text, chunk_size, overlap)):
            result.append(
                Chunk(
                    chunk_id=f"{stem}-p{page.page_number}-c{index}",
                    text=piece,
                    source_file=source_file,
                    page_number=page.page_number,
                    chunk_index=index,
                )
            )
    return result