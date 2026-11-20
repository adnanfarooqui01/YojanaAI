import json
from pathlib import Path

from app.services.retrieval import retrieve

GOLDEN = Path("data/eval/golden.jsonl")
K = 5


def main() -> None:
    rows = [
        json.loads(line)
        for line in GOLDEN.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    found = 0
    reciprocal_ranks = 0.0

    for row in rows:
        hits = retrieve(row["question"], K)
        rank = next(
            (i for i, h in enumerate(hits, 1) if h.page_number in row["expected_pages"]),
            None,
        )
        if rank:
            found += 1
            reciprocal_ranks += 1 / rank
        else:
            print(f"MISS: {row['question']}")

    print(f"\nHit@{K}: {found}/{len(rows)} = {found / len(rows):.0%}")
    print(f"MRR: {reciprocal_ranks / len(rows):.3f}")


if __name__ == "__main__":
    main()