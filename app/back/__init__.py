from http import HTTPStatus

from flask import Flask, request, make_response, jsonify
from flask_cors import CORS

from app.back.constants import UPLOAD_PATH
from app.back.services import imageservice

# from app.back.routes import mainroute

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

app.config["IMAGE_UPLOADS"] = UPLOAD_PATH


@app.route('/', methods=['GET', 'POST', 'DELETE', 'PATCH'])
def upload_image():
    if request.method == 'GET':
        return make_response(jsonify({'response': 'Just testing'}), HTTPStatus.OK)
    elif request.method == 'POST':
        try:
            label = request.args.get('label')
            image = request.files['file']
            if label == '':
                raise Exception('No label present')
            imageservice.save_image(image, label)
            response = 'Image ' + image.filename + ' labeled with ' + label + ' was saved'
            return make_response(jsonify({'resp': response}), 200)
        except Exception as e:
            return make_response(jsonify({'resp': str(e)}), 503)


@app.route('/labels', methods=['GET'])
def process_labels():
    if request.method == 'GET':
        return make_response(jsonify(labels), 200)


@app.route('/images', methods=['GET'])
def get_image_stats():
    if request.method == 'GET':
        stats = imageservice.count_images_for_all_labels(labels)
        return make_response(jsonify(stats), 200)


labels = ['cat', 'dog']
