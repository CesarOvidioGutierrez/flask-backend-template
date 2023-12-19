from flask import request, make_response, jsonify

from app import basic_auth
from app.decorators.decorators import validate_email_decorator, validate_password_length_decorator
from app.utils.jwt import create_token
from app.config.constants import AuthConstants, AuthMessages


@validate_email_decorator
@validate_password_length_decorator
def handle_authentication():
    data = request.get_json()
    email = data.get(AuthConstants.EMAIL.value)
    password = data.get(AuthConstants.PASSWORD.value)

    first_name = AuthConstants.FIRST_NAME.value
    last_name = AuthConstants.LAST_NAME.value
    
    if email and password and basic_auth.check_credentials(email, password):
        token = create_token(email)
        return jsonify({'email': email, 'firstName':first_name, 'lastName': last_name, 'token': token})

    return make_response(jsonify({'message': AuthMessages.INVALID_CREDENTIALS.value}), 401)