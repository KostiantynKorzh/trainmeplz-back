import datetime
import os
import re
from functools import wraps

import jwt
from flask import request

from src.back.setup import logger


def login(username, password):
    logger.info('Attempt to login {}'.format(username))
    true_username, true_password = os.getenv('ADMIN_USERNAME'), os.getenv('ADMIN_PASSWORD')
    if username == true_username and password == true_password:
        logger.info('Password for {} was entered correctly'.format(username))
        return create_jwt(username)

    return Exception('Invalid credentials')


# decorator that uses on routes and let route to accept
# requests only if token is present and valid
def auth_check(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            return 'No token is present'
        token = re.sub('Bearer\s', '', request.headers['Authorization'])
        try:
            is_token_valid(token)
        except Exception as e:
            return 'Invalid token. {}'.format(str(e))
        return function(*args, **kwargs)

    return wrapper


def is_token_valid(token):
    try:
        if os.getenv('ADMIN_USERNAME') != decode_jwt(token):
            raise Exception('Error during validating token')
    except Exception as e:
        logger.info('Error validating token. {}'.format(str(e)))
        raise Exception(str(e))


def create_jwt(username):
    secret_key = os.getenv('SECRET_KEY')
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1),
            'iat': datetime.datetime.utcnow(),
            'sub': username
        }

        token = jwt.encode(
            payload=payload,
            key=secret_key,
            algorithm='HS256'
        )
        logger.info('Creating jwt for {}'.format(username))
        return token
    except Exception as e:
        logger.warning('Error creating jwt. {}'.format(str(e)))


def decode_jwt(token):
    secret_key = os.getenv('SECRET_KEY')
    try:
        payload = jwt.decode(token, secret_key, 'HS256')
        logger.info('Decoding token {}'.format(token))
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'
