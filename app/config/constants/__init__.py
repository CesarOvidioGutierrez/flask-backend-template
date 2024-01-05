from .common import CommonConstants, CommonMessages
from .auth import AuthConstants, AuthMessages

EMAIL = AuthConstants.EMAIL.value
PASSWORD = AuthConstants.PASSWORD.value
FIRST_NAME = AuthConstants.FIRST_NAME.value
LAST_NAME = AuthConstants.LAST_NAME.value

INVALID_CREDENTIALS =  AuthMessages.INVALID_CREDENTIALS.value
PASSWORD_LENGTH_ERROR = AuthMessages.PASSWORD_LENGTH_ERROR.value
INVALID_EMAIL_ERROR = AuthMessages.INVALID_EMAIL_ERROR.value

BASIC_AUTH = CommonConstants.BASIC_AUTH.value
SECRET_KEY = CommonConstants.SECRET_KEY.value
HS256 = CommonConstants.HS256.value
BASIC_AUTH_USERNAME = CommonConstants.BASIC_AUTH_USERNAME.value
BASIC_AUTH_PASSWORD = CommonConstants.BASIC_AUTH_PASSWORD.value
LOG_FILE_NAME = CommonConstants.LOG_FILE_NAME.value

DOCS_VERSION = CommonConstants.DOCS_VERSION.value
DOCS_TITLE = CommonConstants.DOCS_TITLE.value
DOCS_DESCRIPTION = CommonConstants.DOCS_DESCRIPTION.value
    


APP_CREATION_MESSAGE = CommonMessages.APP_CREATION_MESSAGE.value
SUCCESSFUL_AUTH_MESSAGE = CommonMessages.SUCCESSFUL_AUTH_MESSAGE.value
FAILED_AUTH_MESSAGE = CommonMessages.FAILED_AUTH_MESSAGE.value