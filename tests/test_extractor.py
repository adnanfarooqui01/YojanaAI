import fitz

from app.rag.extractor import extract_pages


def test_extract_pages(tmp_path) -> None:
    pdf_path = tmp_path / "sample.pdf"
    doc = fitz.open()
    page = doc.new_page()
    page.insert_text((72, 72), "Eligibility: age 21 to 24")
    doc.save(pdf_path)
    doc.close()

    pages = extract_pages(pdf_path)

    assert len(pages) == 1
    assert "Eligibility" in pages[0].text
