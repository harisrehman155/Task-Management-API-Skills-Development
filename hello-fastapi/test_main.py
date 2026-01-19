from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root_returns_200():
    """GET / returns 200 status."""
    response = client.get("/")
    assert response.status_code == 200


def test_root_returns_message():
    """GET / returns greeting message."""
    response = client.get("/")
    assert "message" in response.json()

def test_greeting_with_name():
    """GET /greet/{name} returns personalized greeting."""
    response = client.get("/greet/Alice")
    assert response.status_code == 200
    assert response.json()["message"] == "Hello, Alice!"