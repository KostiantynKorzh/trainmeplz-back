from flask import make_response, jsonify, request
from flask_apispec import MethodResource, doc, use_kwargs, marshal_with
from flask_restful import Resource
from marshmallow import fields, Schema

from src.back.services import learningservice, labelservice


class TestResponse(Schema):
    prediction = fields.Str()


@doc(tags=['Tests'])
class Test(MethodResource, Resource):

    @doc(description='Send image to get predicted label by model')
    @marshal_with(TestResponse, code=200, description='Model predicted label')
    def post(self):
        image = request.files['file']
        prediction = learningservice.test(image)
        labels = labelservice.get_all_labels()
        return make_response(jsonify(labels[prediction[0]]), 200)
