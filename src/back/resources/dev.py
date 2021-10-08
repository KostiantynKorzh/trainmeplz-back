from flask import make_response, jsonify, request
from flask_apispec import MethodResource, doc, use_kwargs
from flask_restful import Resource, reqparse
from marshmallow import fields

from src.back.services import devservice

parser = reqparse.RequestParser()
parser.add_argument('logLevel', type=str)


@doc(tags=['Dev'])
class Dev(MethodResource, Resource):

    @doc(description='Allows to clear all data for particular label or for all labels at once',
         params={
             'label': {
                 'description': 'Label to empty all data for. Use "all" for all labels at once',
                 'in': 'query', 'type': 'string', 'required': True
             }
         })
    def get(self):
        try:
            args = request.args
            if 'label' in args.keys():
                label_to_delete = args['label']
                print(label_to_delete)
                if label_to_delete == 'all':
                    devservice.empty_all()
                else:
                    devservice.empty_data_for_label_in_db(label_to_delete)
                    devservice.empty_stats_for_label(label_to_delete)
            return make_response(jsonify({'resp': 'testing'}), 200)
        except Exception as e:
            print(str(e))

    @doc(description='Change log level for the application')
    @use_kwargs({'logLevel': fields.Str()})
    def post(self):
        args = parser.parse_args()
        level = args['logLevel']
        devservice.change_log_level(level)
