import json
from pathlib import Path

from app.rag.embedder import embed_passages
from app.rag.schemas import Chunk
from app.rag.vector_store import ensure_collection, upsert_chunks

INPUT = Path("data/processed/chunks.jsonl")
BATCH = 64


def main() -> None:
    chunks = [
        Chunk(**json.loads(line))
        for line in INPUT.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    print(f"Loaded {len(chunks)} chunks")

    ensure_collection()
    for i in range(0, len(chunks), BATCH):
        batch = chunks[i : i + BATCH]
        vectors = embed_passages([c.text for c in batch])
        upsert_chunks(batch, vectors)
        print(f"Indexed {min(i + BATCH, len(chunks))}/{len(chunks)}")

    print("Done.")


if __name__ == "__main__":
    main()