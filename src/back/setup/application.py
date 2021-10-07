from flask import Flask
from flask_cors import CORS

from src.constants import UPLOAD_PATH


def create_app():
    app = Flask(__name__)

    CORS(app, resources={r"*": {"origins": "*"}})

    app.config["IMAGE_UPLOADS"] = UPLOAD_PATH

    # setup_routing(app)
    # swagger.setup_swagger(app)

    return app
