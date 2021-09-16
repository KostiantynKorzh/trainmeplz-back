import os

from flask_pymongo import PyMongo


def setup_db(app):
    dataset_db = init_dataset_db(app)
    article_db = init_article_db(app)

    return dataset_db, article_db


def init_dataset_db(app):
    return init_mongo_db(app, os.environ.get('MONGO_URI', 'mongodb://127.0.0.1:27017/dataset'))


def init_article_db(app):
    return init_mongo_db(app, os.environ.get('MONGO_ARTICLES_URI', 'mongodb://127.0.0.1:27017/articles'))


def init_mongo_db(app, mongo_uri):
    mongo = PyMongo(app, mongo_uri)
    db = mongo.db
    return db
