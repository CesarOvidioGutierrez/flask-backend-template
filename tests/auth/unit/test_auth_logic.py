
import json

def test_valid_email_validation(client):
    data = {'email': 'user@google.com', 'password': 'password123'}
    response = client.post('/api/auth', data=json.dumps(data), content_type='application/json')

    assert response.status_code == 200
    assert 'token' in response.json

def test_invalid_email_validation(client):
    data = {'email': 'invalid_email', 'password': 'password'}
    response = client.post('/api/auth', data=json.dumps(data), content_type='application/json')

    assert response.status_code == 400  
    assert 'message' in response.json

def test_valid_password_validation(client):
    data = {'email': 'user@google.com', 'password': 'password123'}
    response = client.post('/api/auth', data=json.dumps(data), content_type='application/json')

    assert response.status_code == 200
    assert 'token' in response.json

def test_invalid_password_validation(client):
    data = {'email': 'user@google.com', 'password': 'pw'}
    response = client.post('/api/auth', data=json.dumps(data), content_type='application/json')

    assert response.status_code == 400  
    assert 'message' in response.json
