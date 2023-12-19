import json

def test_authentication_with_fixture(client):
    response = client.post('/api/auth', data=json.dumps({'email': 'user@google.com', 'password': 'password123'}), content_type='application/json')
    assert response.status_code == 200
    assert 'token' in response.get_json()

