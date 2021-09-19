from flask import make_response
from flask_restful import Resource


class Stats(Resource):

    def get(self):
        return make_response('All stats here', 200)

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
