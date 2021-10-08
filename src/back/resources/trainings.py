from flask import make_response, jsonify, request
from flask_apispec import MethodResource, doc, marshal_with, use_kwargs
from flask_restful import Resource
from marshmallow import Schema, fields

from src.back.services import imageservice


class TrainingResponse(Schema):
    response = fields.Str()


class TrainingResponseError(Schema):
    error = fields.Str()


@doc(tags=['Trainings'])
class Trainings(MethodResource, Resource):

    @doc(consumes=['multipart/form-data'])
    @marshal_with(TrainingResponse, code=200, description='Confirmation message that image was upload successfully')
    @marshal_with(TrainingResponseError, code=503, description='Returns error')
    def post(self):
        try:
            label = request.args.get('label')
            image = request.files['file']
            if label == '':
                raise Exception('No label present')
            imageservice.save_image(image, label)
            response = 'Image ' + image.filename + ' labeled with ' + label + ' was saved'
            return make_response(jsonify({'response': response}), 200)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 503)
