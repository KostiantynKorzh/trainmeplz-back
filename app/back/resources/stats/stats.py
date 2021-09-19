from flask import make_response
from flask_apispec import MethodResource, doc
from flask_restful import Resource

@doc(tags=['Stats'])
class Stats(MethodResource, Resource):

    def get(self):
        return make_response('All stats here', 200)

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
