from flask_restful import Api

from src.back.resources.auth import Auth
from src.back.resources.stats.images import ImageStats
from src.back.resources.dev import Dev
from src.back.resources.articlelabel import ArticleLabel
from src.back.resources.labels import Label
from src.back.resources.stats.stats import Stats
from src.back.resources.tests import Test
from src.back.resources.trainings import Trainings
from src.back.resources.articles import Article
from src.back.resources.particulararticle import ParticularArticle


def setup_routing(app):
    api = Api(app)

    api.add_resource(Trainings, '/trainings')
    api.add_resource(Test, '/tests')
    api.add_resource(ArticleLabel, '/articles/labels')
    api.add_resource(Label, '/labels')
    api.add_resource(Stats, '/stats')
    api.add_resource(ParticularArticle, '/articles/<string:article_id>')
    api.add_resource(Article, '/articles')
    api.add_resource(ImageStats, '/stats/images')
    api.add_resource(Dev, '/dev')
    api.add_resource(Auth, '/auth')
