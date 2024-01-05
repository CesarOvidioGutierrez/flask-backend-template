# app/decorators.py

import logging

from functools import wraps
from flask import make_response, jsonify, request
from email_validator import validate_email, EmailNotValidError

from app.config.constants import  INVALID_EMAIL_ERROR, PASSWORD_LENGTH_ERROR
def validate_email_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data = request.get_json()
        email = data.get('email')

        try:
            v = validate_email(email)
        except EmailNotValidError as e:
            logging.warning(f'message: {INVALID_EMAIL_ERROR.format(str(e))}')
            return make_response(jsonify({'message': f'{INVALID_EMAIL_ERROR.format(str(e))}'}), 400)

        return func(*args, **kwargs)

    return wrapper

def validate_password_length_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data = request.get_json()
        password = data.get('password')

        if len(password) < 8:
            logging.warning(f'message: {PASSWORD_LENGTH_ERROR}')
            return make_response(jsonify({'message': PASSWORD_LENGTH_ERROR}), 400)

        return func(*args, **kwargs)

    return wrapper
