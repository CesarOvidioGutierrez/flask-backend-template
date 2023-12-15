import jwt
from datetime import datetime, timedelta
from app import app

def create_token(email):
    payload = {
        'exp': datetime.utcnow() + timedelta(days=1),
        'iat': datetime.utcnow(),
        'sub': email
    }
    return jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')

def decode_token(token):
    payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
    return payload
