from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    assert client.get("/health").json()["status"] == "ok"


def test_metric_has_categories():
    body = client.get("/metric").json()
    assert body["current"] > 0
    assert body["by_category"]
