from flask import make_response, jsonify
from flask_apispec import MethodResource, doc, marshal_with, use_kwargs
from flask_restful import Resource
from marshmallow import Schema, fields

from app.back import labels


class CreateLabelsRequestSchema(Schema):
    name = fields.String()


class GetLabelsResponseSchema(Schema):
    response = fields.List(fields.String)


@doc(tags=['Labels'])
class Label(MethodResource, Resource):

    @use_kwargs(CreateLabelsRequestSchema, location='json')
    @marshal_with(GetLabelsResponseSchema)
    def get(self):
        return make_response(jsonify(labels), 200)

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
