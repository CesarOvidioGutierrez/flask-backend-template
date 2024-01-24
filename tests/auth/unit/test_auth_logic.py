
import json
from http import HTTPStatus
from tests import fake_user
from app.config.constants import INVALID_EMAIL_ERROR, PASSWORD_LENGTH_ERROR

expected_fields = ['email', 'firstName', 'lastName', 'token']

def test_valid_email_validation(client, valid_credentials):
    response = client.post('/api/auth', data=json.dumps(valid_credentials), content_type='application/json')

    assert response.status_code == HTTPStatus.OK
    
    for field in expected_fields:
        assert field in response.json

def test_invalid_email_validation(client):
    email, password = fake_user()
    data = {'email': email.split('@')[0], 'password': password}

    response = client.post('/api/auth', data=json.dumps(data), content_type='application/json')

    assert response.status_code == HTTPStatus.BAD_REQUEST  

    assert 'message' in response.json
    assert INVALID_EMAIL_ERROR.split(':')[0] in response.json.get('message')

def test_valid_password_validation(client, valid_credentials):
    response = client.post('/api/auth', data=json.dumps(valid_credentials), content_type='application/json')

    assert response.status_code == HTTPStatus.OK

    for field in expected_fields:
        assert field in response.json

def test_invalid_password_validation(client, valid_credentials):
    _, password = fake_user()
    email = valid_credentials['email']
    data = {'email': email, 'password': password[:4]}

    response = client.post('/api/auth', data=json.dumps(data), content_type='application/json')

    assert response.status_code == HTTPStatus.BAD_REQUEST  

    assert 'message' in response.json
    assert response.json.get('message') == PASSWORD_LENGTH_ERROR

