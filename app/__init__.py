import os, logging


from flask import Flask
from flask_basicauth import BasicAuth

from dotenv import load_dotenv

from .routes import init_app



def create_app():
    logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    app = Flask(__name__)
    logging.info(f'Se crea la app')

    load_dotenv()

    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

    app.config['BASIC_AUTH_USERNAME'] = os.getenv('BASIC_AUTH_USERNAME')
    app.config['BASIC_AUTH_PASSWORD'] = os.getenv('BASIC_AUTH_PASSWORD')

    basic_auth = BasicAuth(app)
    app.config['BASIC_AUTH'] = basic_auth

    init_app(app)

    return app
