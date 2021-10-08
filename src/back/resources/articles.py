import json

from bson import json_util
from flask import make_response, jsonify
from flask_apispec import MethodResource, doc, marshal_with
from flask_restful import Resource, reqparse
from marshmallow import fields, Schema

from src.back.services import articleservice
from src.back.services.authservice import auth_check

parser = reqparse.RequestParser()
parser.add_argument('title', type=str)
parser.add_argument('description', type=str)
parser.add_argument('content', type=str)
parser.add_argument('labelsIds', type=str, action='append')


class ArticleSchema(Schema):
    content = fields.Str()
    description = fields.Str()
    id = fields.Str()
    labels = fields.List(fields.Str())
    title = fields.Str()


class ArticleResponse(Schema):
    artilces = fields.List(fields.Nested(ArticleSchema))


@doc(tags=['Articles'])
class Article(MethodResource, Resource):

    @doc(description='Get all articles')
    @marshal_with(ArticleResponse)
    def get(self):
        data = json.loads(json_util.dumps(articleservice.get_all_articles()))
        return make_response(jsonify({'articles': data}))

    @auth_check
    def post(self):
        args = parser.parse_args()
        title = args['title']
        description = args['description']
        content = args['content']
        labels_ids = args['labelsIds']

        return articleservice.create_article(title, description, content, labels_ids)

    def get_by_id(self, article_id):
        print(article_id)
