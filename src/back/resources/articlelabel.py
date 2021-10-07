import json

from bson import json_util
from flask_apispec import MethodResource, doc
from flask_restful import Resource

from src.back.services import articlelabelservice
from src.back.services.authservice import auth_check


@doc(tags=['Article labels'])
class ArticleLabel(MethodResource, Resource):

    def get(self):
        return json.loads(json_util.dumps(articlelabelservice.get_all_labels()))

    @auth_check
    def post(self):
        articlelabelservice.create_label('third')

    @auth_check
    def put(self):
        pass

    @auth_check
    def delete(self):
        pass
