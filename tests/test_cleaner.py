from app.rag.cleaner import clean_text


def test_joins_broken_lines_and_collapses_spaces() -> None:
    assert clean_text("Eligible   candidates\nmust apply") == (
        "Eligible candidates must apply"
    )


def test_keeps_paragraph_breaks() -> None:
    assert clean_text("Para one.\n\nPara two.") == "Para one.\n\nPara two."


def test_collapses_spaces_created_when_joining_lines() -> None:
    assert clean_text("A \n B") == "A B"
