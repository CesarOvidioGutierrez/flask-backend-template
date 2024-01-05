import os, logging

from flask import Flask
from flask_basicauth import BasicAuth

from dotenv import load_dotenv

from .routes import auth_blueprint, ns_auth
from .config.constants import CommonConstants, CommonMessages
from .config.extensions import api



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

    app.register_blueprint(auth_blueprint, url_prefix='/api', name='auth')

    api.init_app(app, version=CommonConstants.DOCS_VERSION.value, title=CommonConstants.DOCS_TITLE.value, description=CommonConstants.DOCS_DESCRIPTION.value)
    api.add_namespace(ns_auth)

    return app
