from flask import Flask
from flask_cors import CORS

from app.constants import UPLOAD_PATH

app = Flask(__name__)

cors = CORS(app, resources={r"*": {"origins": "*"}})

app.config["IMAGE_UPLOADS"] = UPLOAD_PATH
