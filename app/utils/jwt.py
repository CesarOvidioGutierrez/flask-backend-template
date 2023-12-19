import jwt
from datetime import datetime, timedelta
from flask import current_app


def create_token(email):
    secret_key = current_app.config['SECRET_KEY']
    payload = {
        'exp': datetime.utcnow() + timedelta(days=1),
        'iat': datetime.utcnow(),
        'sub': email
    }
    return jwt.encode(payload, secret_key, algorithm='HS256')

def decode_token(token):
    secret_key = current_app.config['SECRET_KEY']
    payload = jwt.decode(token, secret_key, algorithms=['HS256'])
    return payload
