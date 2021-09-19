from flask import make_response, jsonify
from flask_restful import Resource

from app.back import labels
from app.back.services import labelservice


class ImageStats(Resource):
    def get(self):
        stats = labelservice.count_images_for_all_labels(labels)
        return make_response(jsonify(stats), 200)

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
