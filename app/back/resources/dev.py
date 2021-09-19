from flask import make_response, jsonify
from flask_restful import Resource

from app.back.services import devservice


class Dev(Resource):

    def get(self):
        try:
            devservice.empty_data_for_all_labels_in_db()
            return make_response(jsonify({'resp': 'testing'}), 200)
        except Exception as e:
            print(str(e))

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
