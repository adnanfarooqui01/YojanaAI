from app.rag.vector_store import chunk_to_point_id


def test_point_id_is_deterministic():
    assert chunk_to_point_id("a-p1-c0") == chunk_to_point_id("a-p1-c0")


def test_point_id_differs_per_chunk():
    assert chunk_to_point_id("a-p1-c0") != chunk_to_point_id("a-p1-c1")