import sys

from app.rag.embedder import embed_query
from app.rag.vector_store import search

question = " ".join(sys.argv[1:]) or "Who is eligible for PMAY Urban?"
for hit in search(embed_query(question), limit=5):
    p = hit.payload
    print(f"\nscore={hit.score:.3f}  {p['source_file']}  page {p['page_number']}")
    print(p["text"][:300])