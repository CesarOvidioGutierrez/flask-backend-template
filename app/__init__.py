import os, logging

from flask import Flask
from flask_basicauth import BasicAuth

from dotenv import load_dotenv

from .routes import auth_blueprint, ns_auth
from .config.constants import  (LOG_FILE_NAME, APP_CREATION_MESSAGE, SECRET_KEY, BASIC_AUTH_USERNAME, 
                                BASIC_AUTH_PASSWORD, BASIC_AUTH, DOCS_VERSION, DOCS_TITLE, DOCS_DESCRIPTION )

from .config.extensions import api



def create_app():
    logging.basicConfig(filename=LOG_FILE_NAME, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    app = Flask(__name__)
    logging.info(APP_CREATION_MESSAGE)

    load_dotenv()

    app = Flask(__name__)
    app.config[SECRET_KEY] = os.getenv(SECRET_KEY)

    app.config[BASIC_AUTH_USERNAME] = os.getenv(BASIC_AUTH_USERNAME)
    app.config[BASIC_AUTH_PASSWORD] = os.getenv(BASIC_AUTH_PASSWORD)

    basic_auth = BasicAuth(app)
    app.config[BASIC_AUTH] = basic_auth

    app.register_blueprint(auth_blueprint, url_prefix='/api', name='auth')

    api.init_app(app, version=DOCS_VERSION, title=DOCS_TITLE, description=DOCS_DESCRIPTION)
    api.add_namespace(ns_auth)

    return app
