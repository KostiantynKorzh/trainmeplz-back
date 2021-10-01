from flask import make_response, jsonify, request
from flask_apispec import MethodResource, doc
from flask_restful import Resource

from app.back.services import imageservice

@doc(tags=['Trains'])
class Train(MethodResource, Resource):

    def get(self):
        pass

    def post(self):
        try:
            label = request.args.get('label')
            image = request.files['file']
            # if label == '':
            #     raise Exception('No label present')
            imageservice.save_image(image, label)
            response = 'Image ' + image.filename + ' labeled with ' + label + ' was saved'
            return make_response(jsonify({'resp': response}), 200)
        except Exception as e:
            return make_response(jsonify({'resp': str(e)}), 503)

    def put(self):
        pass

    def delete(self):
        pass
