from flask import make_response, jsonify, request
from flask_apispec import MethodResource, doc
from flask_restful import Resource

from app.back.services import learningservice, labelservice


@doc(tags=['Tests'])
class Test(MethodResource, Resource):

    def get(self):
        pass

    def post(self):
        image = request.files['file']
        prediction = learningservice.test(image)
        labels = labelservice.get_all_labels()
        return make_response(jsonify(labels[prediction[0]]), 200)

    def put(self):
        pass

    def delete(self):
        pass
