from http import HTTPStatus

from flask import make_response, jsonify, request
from flask_apispec import MethodResource
from flask_restful import Resource, reqparse

from src.back.services import authservice

parser = reqparse.RequestParser()
parser.add_argument('username', type=str)
parser.add_argument('password', type=str)


class Auth(MethodResource, Resource):

    def get(self):
        try:
            token = request.args.get('token')
            authservice.is_token_valid(token)
            return 'Successfully validated'
        except Exception as e:
            return make_response(jsonify(str(e)), HTTPStatus.BAD_REQUEST)

    def post(self):
        try:
            args = parser.parse_args()
            username = args['username']
            password = args['password']

            return authservice.login(username, password)
        except Exception as e:
            return make_response(jsonify(str(e)), HTTPStatus.BAD_REQUEST)
