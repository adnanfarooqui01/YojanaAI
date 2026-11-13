from pathlib import Path

import pymupdf

from app.rag.schemas import Page


def extract_pages(pdf_path: Path) -> list[Page]:
    pages: list[Page] = []
    with pymupdf.open(pdf_path) as doc:
        for number, page in enumerate(doc, start=1):
            text = page.get_text("text")
            if text.strip():
                pages.append(Page(page_number=number, text=text))
    return pages