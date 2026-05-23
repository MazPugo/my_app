from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_all_endpoints_respond():
    root = client.get("/")
    health = client.get("/health")
    assert root.status_code == 200
    assert health.status_code == 200


def test_invalid_endpoint_returns_404():
    response = client.get("/does-not-exist")
    assert response.status_code == 404


def test_root_returns_correct_format():
    response = client.get("/")
    data = response.json()
    assert isinstance(data, dict)
    assert "message" in data


def test_health_returns_correct_format():
    response = client.get("/health")
    data = response.json()
    assert isinstance(data, dict)
    assert "status" in data
    assert data["status"] == "ok"
