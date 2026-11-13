import json
from pathlib import Path

from app.core.config import get_settings
from app.rag.chunker import chunk_pages
from app.rag.cleaner import clean_text
from app.rag.extractor import extract_pages
from app.rag.schemas import Page

DOCS_DIR = Path("documents")
OUTPUT = Path("data/processed/chunks.jsonl")


def main() -> None:
    settings = get_settings()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    total = 0
    with OUTPUT.open("w", encoding="utf-8") as out:
        for pdf in sorted(DOCS_DIR.glob("*.pdf")):
            pages = [
                Page(page_number=p.page_number, text=clean_text(p.text))
                for p in extract_pages(pdf)
            ]
            chunks = chunk_pages(
                pages, pdf.name, settings.chunk_size, settings.chunk_overlap
            )
            for chunk in chunks:
                out.write(json.dumps(chunk.model_dump(), ensure_ascii=False) + "\n")
            print(f"{pdf.name}: {len(pages)} pages -> {len(chunks)} chunks")
            total += len(chunks)

    print(f"Done. {total} chunks written to {OUTPUT}")


if __name__ == "__main__":
    main()