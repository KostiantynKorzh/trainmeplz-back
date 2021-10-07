from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec import FlaskApiSpec

from src.back.resources.articlelabel import ArticleLabel
from src.back.resources.articles import Article
from src.back.resources.auth import Auth
from src.back.resources.dev import Dev
from src.back.resources.labels import Label
from src.back.resources.particulararticle import ParticularArticle
from src.back.resources.stats.images import ImageStats
from src.back.resources.stats.stats import Stats
from src.back.resources.tests import Test
from src.back.resources.trains import Train


def setup_swagger(app):
    app.config.update({
        'APISPEC_SPEC': APISpec(
            title='trainmeplz.com',
            version='v1',
            plugins=[MarshmallowPlugin()],
            openapi_version='2.0.0'
        ),
        'APISPEC_SWAGGER_URL': '/swagger/',
        'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'
    })

    register_resources(app)


def register_resources(app):
    docs = FlaskApiSpec(app)

    docs.register(Stats)
    docs.register(ImageStats)
    docs.register(Dev)
    docs.register(Label)
    docs.register(Test)
    docs.register(Train)
    docs.register(ArticleLabel)
    docs.register(ParticularArticle)
    docs.register(Article)
    docs.register(Auth)
