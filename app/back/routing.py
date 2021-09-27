from flask_restful import Api

from app.back.application import app
from app.back.resources.stats.images import ImageStats

api = Api(app)

from app.back.resources.dev import Dev
from app.back.resources.articlelabel import ArticleLabel
from app.back.resources.labels import Label
from app.back.resources.stats.stats import Stats
from app.back.resources.tests import Test
from app.back.resources.trains import Train
from app.back.resources.articles import Article

try:
    api.add_resource(Train, '/trains')
    api.add_resource(Test, '/tests')
    api.add_resource(ArticleLabel, '/articles/labels')
    api.add_resource(Label, '/labels')
    api.add_resource(Stats, '/stats')
    api.add_resource(Article, '/articles')
    api.add_resource(ImageStats, '/stats/images')
    api.add_resource(Dev, '/dev')
except Exception as e:
    print(str(e))
