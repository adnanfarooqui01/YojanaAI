from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_search_rejects_short_query():
    response = client.post("/api/v1/search", json={"query": "a"})
    assert response.status_code == 422


def test_search_rejects_huge_top_k():
    response = client.post("/api/v1/search", json={"query": "EWS income", "top_k": 500})
    assert response.status_code == 422