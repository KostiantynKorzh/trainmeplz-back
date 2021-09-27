import json

from bson import json_util
from flask_apispec import MethodResource, doc
from flask_restful import Resource, reqparse

from app.back.services import articleservice

parser = reqparse.RequestParser()
parser.add_argument('title', type=str)
parser.add_argument('description', type=str)
parser.add_argument('content', type=str)
parser.add_argument('labelsIds', type=str, action='append')


@doc(tags=['Articles'])
class Article(MethodResource, Resource):

    def get(self):
        return json.loads(json_util.dumps(articleservice.get_all_articles()))
        # return articleservice.create_article('1', '2', '3', ['615186a12770edad1a24fbc7', '615192502108f7d4e5179c9e'])

    def post(self):
        args = parser.parse_args()
        title = args['title']
        description = args['description']
        content = args['content']
        labels_ids = args['labelsIds']

        return articleservice.create_article(title, description, content, labels_ids)

    def put(self):
        pass

    def delete(self):
        pass