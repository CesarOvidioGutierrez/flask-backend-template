import logging
from flask import request, make_response, jsonify, current_app

from app.decorators.decorators import validate_email_decorator, validate_password_length_decorator
from app.utils.jwt import create_token
from app.config.constants import AuthConstants, AuthMessages, CommonConstants, CommonMessages


@validate_email_decorator
@validate_password_length_decorator
def handle_authentication():
    data = request.get_json()
    email = data.get(AuthConstants.EMAIL.value)
    password = data.get(AuthConstants.PASSWORD.value)

    first_name = AuthConstants.FIRST_NAME.value
    last_name = AuthConstants.LAST_NAME.value

    basic_auth = current_app.config[CommonConstants.BASIC_AUTH]
    
    if email and password and basic_auth.check_credentials(email, password):
        token = create_token(email)
        logging.info(CommonMessages.SUCCESSFUL_AUTH_MESSAGE.value.format(email))

        return jsonify({'email': email, 'firstName':first_name, 'lastName': last_name, 'token': token})

    logging.warning(CommonMessages.FAILED_AUTH_MESSAGE.value.format(email))
    return make_response(jsonify({'message': AuthMessages.INVALID_CREDENTIALS.value}), 401)
