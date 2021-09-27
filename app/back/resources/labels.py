from flask import make_response, jsonify
from flask_apispec import MethodResource, doc, marshal_with
from flask_restful import Resource
from marshmallow import Schema, fields

from app.back.services import labelservice


class GetLabelsResponseSchema(Schema):
    response = fields.List(fields.String)


@doc(tags=['Labels'])
class Label(MethodResource, Resource):

    @marshal_with(GetLabelsResponseSchema)
    def get(self):
        labels = labelservice.get_all_labels()
        return make_response(jsonify(labels), 200)

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
