import os

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask import Flask
from flask_apispec import FlaskApiSpec
from flask_cors import CORS

from app.back.services.storage.azureblobimagestorageservice import AzureBlobImageStorageService
from app.back.services.storage.imagestorageservice import ImageStorageService
from app.constants import UPLOAD_PATH

app = Flask(__name__)

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

image_storage_approach = os.getenv('IMAGE_STORAGE_APPROACH')

if image_storage_approach == 'blob':
    imagestorageservice = AzureBlobImageStorageService()
else:
    imagestorageservice = ImageStorageService()
