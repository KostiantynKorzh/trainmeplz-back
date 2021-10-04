from http import HTTPStatus

from flask import make_response, jsonify
from flask_apispec import MethodResource, doc, marshal_with
from flask_restful import Resource
from marshmallow import Schema, fields

from app.back.services import labelservice


class GetImageStatsResponse(Schema):
    label_name1 = fields.Integer()
    label_name2 = fields.Integer()


@doc(tags=['Image Stats'])
class ImageStats(MethodResource, Resource):

    @doc(description='Get stats about quantity of images in dataset for each label')
    @marshal_with(GetImageStatsResponse, HTTPStatus.OK)
    def get(self):
        stats = labelservice.get_stats_for_all_labels()
        return make_response(jsonify(stats), HTTPStatus.OK)
