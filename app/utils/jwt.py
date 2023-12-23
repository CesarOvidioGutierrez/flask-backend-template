import jwt

from flask import current_app

from datetime import datetime, timedelta

from ..config.constants import CommonConstants

def create_token(email):
    secret_key = current_app.config[CommonConstants.SECRET_KEY.value]
    payload = {
        'exp': datetime.utcnow() + timedelta(days=1),
        'iat': datetime.utcnow(),
        'sub': email
    }
    return jwt.encode(payload, secret_key, algorithm=CommonConstants.HS256.value)

def decode_token(token):
    secret_key = current_app.config[CommonConstants.SECRET_KEY.value]
    payload = jwt.decode(token, secret_key, algorithms=[CommonConstants.HS256.value])
    return payload
