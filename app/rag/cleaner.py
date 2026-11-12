import re


def clean_text(text: str) -> str:
    text = text.replace("\x00", "")
    text = re.sub(r"[ \t]+", " ", text)            # collapse spaces/tabs
    text = re.sub(r"-\n(\w)", r"\1", text)         # join words split by hyphen at line end
    text = re.sub(r"\n{3,}", "\n\n", text)         # max one blank line
    text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)   # single newline inside a paragraph -> space
    return text.strip()