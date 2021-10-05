import os

from flask_pymongo import PyMongo

from app.back.application import app
from app.back.repositories.articlelabelrepo import ArticleLabelRepo
from app.back.repositories.articlerepo import ArticleRepo


from app.back.services.storage.azureblobimagestorageservice import AzureBlobImageStorageService
from app.back.services.storage.mongoimagestorageservice import MongoImageStorageService

mongo_uri = os.environ.get('MONGO_URI', 'mongodb://127.0.0.1:27017/dataset')
mongo_articles_uri = os.environ.get('MONGO_ARTICLES_URI', 'mongodb://127.0.0.1:27017/articles')

mongo = PyMongo(app, mongo_uri)
db = mongo.db

mongo_articles = PyMongo(app, mongo_articles_uri)
db_articles = mongo_articles.db

image_storage_approach = os.getenv('IMAGE_STORAGE_APPROACH')

from app.back.repositories.labelrepo import LabelRepo
labelrepo = LabelRepo(db)

if image_storage_approach == 'blob':
    imagestorageservice = AzureBlobImageStorageService()
else:
    imagestorageservice = MongoImageStorageService(db)

from app.back.repositories.repo import Repo


# imagerepo = ImageRepo(db)

repo = Repo(db)
articlerepo = ArticleRepo(db_articles)
articlelabelrepo = ArticleLabelRepo(db_articles)
# imagerepo = ImageRepo(db, None)