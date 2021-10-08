import json

from bson import json_util
from flask_apispec import MethodResource, doc
from flask_restful import Resource, reqparse

from src.back.services import articleservice
from src.back.services.authservice import auth_check

parser = reqparse.RequestParser()
parser.add_argument('title', type=str)
parser.add_argument('description', type=str)
parser.add_argument('content', type=str)
parser.add_argument('labelsIds', type=str, action='append')


@doc(tags=['Articles'])
class ParticularArticle(MethodResource, Resource):

    def get(self, article_id):
        return json.loads(json_util.dumps(articleservice.get_article_by_id(article_id)))

    @auth_check
    def put(self, article_id):
        args = parser.parse_args()
        title = args['title']
        description = args['description']
        content = args['content']
        labels_ids = args['labelsIds']

        articleservice.update_article(article_id, title, description, content, labels_ids)

    @auth_check
    def delete(self, article_id):
        articleservice.delete_article(article_id)
