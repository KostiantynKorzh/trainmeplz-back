from flask_apispec import MethodResource
from flask_restful import Resource, reqparse

from app.back.services import authservice

parser = reqparse.RequestParser()
parser.add_argument('username', type=str)
parser.add_argument('password', type=str)


class Auth(MethodResource, Resource):

    def get(self):
        pass

    def post(self):
        args = parser.parse_args()
        username = args['username']
        password = args['password']

        return authservice.login(username, password)
