import json

from bson import json_util
from flask_apispec import MethodResource, doc
from flask_restful import Resource

from app.back.services import articlelabelservice


@doc(tags=['Article labels'])
class ArticleLabel(MethodResource, Resource):

    def get(self):
        return json.loads(json_util.dumps(articlelabelservice.get_all_labels()))

    def post(self):
        articlelabelservice.create_label('first')

    def put(self):
        pass

    def delete(self):
        pass
