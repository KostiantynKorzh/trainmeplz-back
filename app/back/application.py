import logging

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask import Flask
from flask_apispec import FlaskApiSpec
from flask_cors import CORS

from app.constants import UPLOAD_PATH

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(threadName)s %(pathname)s : %(message)s')

cors = CORS(app, resources={r"*": {"origins": "*"}})

app.config["IMAGE_UPLOADS"] = UPLOAD_PATH

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

logger = app.logger

docs = FlaskApiSpec(app)
