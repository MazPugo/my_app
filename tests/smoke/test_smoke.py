import requests
import os

BASE_URL = os.getenv("APP_URL", "http://localhost:8080")


def test_app_is_live():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200


def test_health_is_live():
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200


def test_health_returns_ok():
    response = requests.get(f"{BASE_URL}/health")
    assert response.json()["status"] == "ok"


def test_response_is_json():
    response = requests.get(f"{BASE_URL}/")
    assert response.headers["content-type"] == "application/json"
