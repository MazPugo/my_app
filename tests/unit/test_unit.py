from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_hello_world_status():
    response = client.get("/")
    assert response.status_code == 200

def test_hello_world_message():
    response = client.get("/")
    assert "message" in response.json()

def test_health_status():
    response = client.get("/health")
    assert response.status_code == 200

def test_health_returns_ok():
    response = client.get("/health")
    assert response.json() == {"status": "ok"}




