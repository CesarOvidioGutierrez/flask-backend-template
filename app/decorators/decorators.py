# app/decorators.py

import logging

from functools import wraps
from flask import make_response, jsonify, request
from email_validator import validate_email, EmailNotValidError

from app.config.constants import  AuthMessages

def validate_email_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data = request.get_json()
        email = data.get('email')

        try:
            v = validate_email(email)
        except EmailNotValidError as e:
            logging.warning(f'message: {AuthMessages.INVALID_EMAIL_ERROR.value.format(str(e))}')
            return make_response(jsonify({'message': f'{AuthMessages.INVALID_EMAIL_ERROR.value.format(str(e))}'}), 400)

        return func(*args, **kwargs)

    return wrapper

def validate_password_length_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        data = request.get_json()
        password = data.get('password')

        if len(password) < 8:
            logging.warning(f'message: {AuthMessages.PASSWORD_LENGTH_ERROR.value}')
            return make_response(jsonify({'message': AuthMessages.PASSWORD_LENGTH_ERROR.value}), 400)

        return func(*args, **kwargs)

    return wrapper
