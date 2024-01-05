from enum import Enum

class AuthConstants(Enum):
    EMAIL = 'email'
    PASSWORD = 'password'
    FIRST_NAME = 'First Name'
    LAST_NAME = 'Last Name'

class AuthMessages(Enum):
    INVALID_CREDENTIALS = 'Invalid credentials'
    PASSWORD_LENGTH_ERROR = f'{AuthConstants.PASSWORD.value} must be at least 8 characters'
    INVALID_EMAIL_ERROR = f'Invalid {AuthConstants.EMAIL.value}: {{}}'

