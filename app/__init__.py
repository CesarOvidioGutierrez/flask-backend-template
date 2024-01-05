import os, logging

from flask import Flask
from flask_basicauth import BasicAuth

from dotenv import load_dotenv

from .routes import init_app
from .config.constants import CommonConstants, CommonMessages



def create_app():
    logging.basicConfig(filename=CommonConstants.LOG_FILE_NAME.value, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    app = Flask(__name__)
    logging.info(CommonMessages.APP_CREATION_MESSAGE.value)

    load_dotenv()

    app = Flask(__name__)
    app.config[CommonConstants.SECRET_KEY.value] = os.getenv(CommonConstants.SECRET_KEY.value)

    app.config[CommonConstants.BASIC_AUTH_USERNAME.value] = os.getenv(CommonConstants.BASIC_AUTH_USERNAME.value)
    app.config[CommonConstants.BASIC_AUTH_PASSWORD.value] = os.getenv(CommonConstants.BASIC_AUTH_PASSWORD.value)

    basic_auth = BasicAuth(app)
    app.config[CommonConstants.BASIC_AUTH] = basic_auth

    init_app(app)

    return app
