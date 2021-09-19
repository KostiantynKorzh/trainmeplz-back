from flask import make_response, jsonify
from flask_apispec import MethodResource, doc
from flask_restful import Resource

from app.back import labels


@doc(tags=['Labels'])
class Label(MethodResource, Resource):

    def get(self):
        return make_response(jsonify(labels), 200)

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
