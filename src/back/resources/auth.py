from http import HTTPStatus

from flask import make_response, jsonify, request
from flask_apispec import MethodResource, doc, use_kwargs, marshal_with
from flask_restful import Resource, reqparse
from marshmallow import fields, Schema

from src.back.services import authservice

parser = reqparse.RequestParser()
parser.add_argument('username', type=str)
parser.add_argument('password', type=str)


class LoginResponse(Schema):
    token = fields.Str()


@doc(tags=['Auth'])
class Auth(MethodResource, Resource):

    @doc(description='Validate JWT',
         params={
             'token': {
                 'description': 'Token to validate',
                 'in': 'query', 'type': 'string', 'required': True
             }
         })
    def get(self):
        try:
            token = request.args.get('token')
            authservice.is_token_valid(token)
            return 'Successfully validated'
        except Exception as e:
            return make_response(jsonify(str(e)), HTTPStatus.BAD_REQUEST)

    @doc(description='Send login request to server. If successful, returns JWT')
    @use_kwargs({'username': fields.Str(), 'password': fields.Str()})
    @marshal_with(LoginResponse)
    def post(self):
        try:
            args = parser.parse_args()
            username = args['username']
            password = args['password']

            return authservice.login(username, password)
        except Exception as e:
            return make_response(jsonify(str(e)), HTTPStatus.BAD_REQUEST)
