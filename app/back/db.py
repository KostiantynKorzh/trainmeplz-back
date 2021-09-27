import os

import gridfs
from flask_pymongo import PyMongo

from app.back.application import app
from app.back.repositories.imagerepo import ImageRepo
from app.back.repositories.labelrepo import LabelRepo
from app.back.repositories.repo import Repo

mongo_uri = os.environ.get('MONGO_URI', 'mongodb://127.0.0.1:27017/grid-test')

mongo = PyMongo(app, mongo_uri)
db = mongo.db

grid_fs = gridfs.GridFS(db)

imagerepo = ImageRepo(db, grid_fs)
labelrepo = LabelRepo(db)
repo = Repo(db)
