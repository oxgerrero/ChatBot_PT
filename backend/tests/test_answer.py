from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

@pytest.fixture
def mock_memory(monkeypatch):
    class DummyMemory:
        def get_history(self, session_id):
            return []
        def append(self, session_id, message):
            pass
    monkeypatch.setattr("app.api.routes.memory", DummyMemory())

def test_answer_ok(mock_memory):
    response = client.post("/answer", json={
        "question": "¿Cuál es la capital de Francia?",
        "session_id": "test_session"
    })
    assert response.status_code == 200
    assert "answer" in response.json()

def test_answer_empty_question(mock_memory):
    response = client.post("/answer", json={
        "question": "",
        "session_id": "test_session"
    })
    assert response.status_code == 422
