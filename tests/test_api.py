import os
os.environ["DATABASE_URL"] = "sqlite:///test.db"

import pytest
from app.wsgi import app, db

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200

def test_create_task(client):
    r = client.post("/api/tasks", json={"title": "Test task"})
    assert r.status_code == 201
    assert r.get_json()["title"] == "Test task"

def test_get_tasks(client):
    r = client.get("/api/tasks")
    assert r.status_code == 200
    assert isinstance(r.get_json(), list)

def test_create_task_no_title(client):
    r = client.post("/api/tasks", json={})
    assert r.status_code == 400
