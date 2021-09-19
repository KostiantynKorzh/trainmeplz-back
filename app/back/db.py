from flask_pymongo import PyMongo

from app.back.application import app

app.config['MONGO_URI'] = 'mongodb://localhost:27017/dataset'
mongo = PyMongo(app)
db = mongo.db
