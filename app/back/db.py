import os

from flask_pymongo import PyMongo

from app.back.application import app
from app.back.repositories.articlelabelrepo import ArticleLabelRepo
from app.back.repositories.articlerepo import ArticleRepo
from app.back.repositories.imagerepo import ImageRepo
from app.back.repositories.labelrepo import LabelRepo
from app.back.repositories.repo import Repo

mongo_uri = os.environ.get('MONGO_URI', 'mongodb://127.0.0.1:27017/dataset')
mongo_articles_uri = os.environ.get('MONGO_ARTICLES_URI', 'mongodb://127.0.0.1:27017/articles')

mongo = PyMongo(app, mongo_uri)
db = mongo.db

mongo_articles = PyMongo(app, mongo_articles_uri)
db_articles = mongo_articles.db

imagerepo = ImageRepo(db)
labelrepo = LabelRepo(db)
repo = Repo(db)
articlerepo = ArticleRepo(db_articles)
articlelabelrepo = ArticleLabelRepo(db_articles)
