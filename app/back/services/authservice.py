import datetime
import re
from functools import wraps

import jwt
from flask import request


def login(username, password):
    true_username, true_password = 'admin', 'password'
    if username == true_username and password == true_password:
        return create_jwt(username)

    return 'Invalid credentials'


def auth_check(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            return 'No token is present'
        token = re.sub('Bearer\s', '', request.headers['Authorization'])
        try:
            is_token_valid(token)
        except Exception as e:
            return 'Invalid token: {}'.format(str(e))
        return function(*args, **kwargs)

    return wrapper


def is_token_valid(token):
    print(decode_jwt(token))
    if 'admin' != decode_jwt(token):
        raise Exception('Wrong sub')


def create_jwt(username):
    secret_key = 'aboba'
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1),
            'iat': datetime.datetime.utcnow(),
            'sub': username
        }
        return jwt.encode(
            payload=payload,
            key=secret_key,
            algorithm='HS256'
        )
    except Exception as e:
        print(str(e))


def decode_jwt(token):
    secret_key = 'aboba'
    try:
        payload = jwt.decode(token, secret_key, 'HS256')
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'
