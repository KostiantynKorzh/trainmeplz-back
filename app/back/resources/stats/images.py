from flask import make_response, jsonify
from flask_apispec import MethodResource, doc
from flask_restful import Resource

from app.back.services import labelservice


@doc(tags=['Image Stats'])
class ImageStats(MethodResource, Resource):

    def get(self):
        labels = labelservice.get_all_labels()
        stats = labelservice.count_images_for_all_labels(labels)
        return make_response(jsonify(stats), 200)

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
