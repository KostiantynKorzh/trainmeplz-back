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
class Article(MethodResource, Resource):

    def get(self):
        return json.loads(json_util.dumps(articleservice.get_all_articles()))

    @auth_check
    def post(self):
        args = parser.parse_args()
        title = args['title']
        description = args['description']
        content = args['content']
        labels_ids = args['labelsIds']

        return articleservice.create_article(title, description, content, labels_ids)

    @auth_check
    def put(self):
        pass

    @auth_check
    def delete(self):
        pass

    def get_by_id(self, article_id):
        print(article_id)
