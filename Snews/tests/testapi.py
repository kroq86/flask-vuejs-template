import pytest
from app import app

@pytest.fixture(scope="module")
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_api(client):
    resp = client.get('/posts')
    assert resp.status_code == 200

def test_resource_one(client):
    resp = client.get('/posts/1')
    assert resp.status_code == 200

def test_resource_one_post(client):
    resp = client.post('/posts/1')
    assert resp.status_code == 201

def test_resource_one_patch(client):
    resp = client.patch('/posts/1')
    assert resp.status_code == 405

def test_secure_resource_fail(client):
    resp = client.get('/posts/1')
    assert resp.status_code == 401

