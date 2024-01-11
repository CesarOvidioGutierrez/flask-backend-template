import logging
from flask import request, make_response, jsonify, current_app
from http import HTTPStatus


from app.decorators import validate_email_decorator, validate_password_length_decorator
from app.utils import create_token
from app.config.constants import EMAIL, PASSWORD, FIRST_NAME, LAST_NAME, BASIC_AUTH, SUCCESSFUL_AUTH_MESSAGE, FAILED_AUTH_MESSAGE, INVALID_CREDENTIALS


@validate_email_decorator
@validate_password_length_decorator
def handle_authentication():
    try:
        data = request.get_json()
        email = data.get(EMAIL)
        password = data.get(PASSWORD)

        first_name = FIRST_NAME
        last_name = LAST_NAME

        basic_auth = current_app.config[BASIC_AUTH]
        
        if email and password and basic_auth.check_credentials(email, password):
            token = create_token(email)
            logging.info(SUCCESSFUL_AUTH_MESSAGE.format(email))

            response_data = {'email': email, 'firstName':first_name, 'lastName': last_name, 'token': token}
            return make_response(jsonify(response_data), HTTPStatus.OK)
        
        else:
            logging.warning(FAILED_AUTH_MESSAGE.format(email))
            return make_response(jsonify({'message': INVALID_CREDENTIALS}), HTTPStatus.UNAUTHORIZED)
    except Exception as e:
        logging.error(f"Error during authentication: {str(e)}")
        return make_response(jsonify({'message': 'Internal Server Error'}), HTTPStatus.INTERNAL_SERVER_ERROR)