from enum import Enum

class CommonConstants(Enum):
    BASIC_AUTH = 'BASIC_AUTH'
    SECRET_KEY = 'SECRET_KEY'
    HS256 = 'HS256'
    BASIC_AUTH_USERNAME = 'BASIC_AUTH_USERNAME'
    BASIC_AUTH_PASSWORD = 'BASIC_AUTH_PASSWORD'
    LOG_FILE_NAME = 'app.log'
    # Flask-restx for docs
    DOCS_VERSION = '1.0'
    DOCS_TITLE = 'Flask Backend Template'
    DOCS_DESCRIPTION = 'A simple API'
    

class CommonMessages(Enum):
    APP_CREATION_MESSAGE = 'Application created'
    SUCCESSFUL_AUTH_MESSAGE = 'Authentication successful for user {}'
    FAILED_AUTH_MESSAGE = 'Authentication attempt failed for user {}'
