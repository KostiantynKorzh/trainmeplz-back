from flask import make_response, jsonify
from flask_restful import Resource

from app.back import labels


class Label(Resource):

    def get(self):
        return make_response(jsonify(labels), 200)

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
