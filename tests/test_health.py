from fastapi.testclient import TestClient

from app.main import app, create_app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_app_metadata() -> None:
    test_app = create_app()

    assert test_app.title == "YojanaAI"
    assert test_app.description == "Indian Government Scheme AI Assistant"
    assert test_app.version == "0.1.0"
