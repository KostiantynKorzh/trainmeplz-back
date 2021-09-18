from http import HTTPStatus

from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo

from app.back.constants import UPLOAD_PATH

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

app.config['MONGO_URI'] = 'mongodb://localhost:27017/dataset'
mongo = PyMongo(app)
db = mongo.db

app.config["IMAGE_UPLOADS"] = UPLOAD_PATH

from app.back.services import imageservice, devservice, labelservice, learningservice


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
            imageservice.convert_image_to_data_and_save(image, label)
            response = 'Image ' + image.filename + ' labeled with ' + label + ' was saved'
            return make_response(jsonify({'resp': response}), 200)
        except Exception as e:
            return make_response(jsonify({'resp': str(e)}), 503)


@app.route('/labels', methods=['GET'])
def process_labels():
    if request.method == 'GET':
        # entry = db.model.find_one({'label': 'cat'})
        # print(entry['_id'])
        # entry['images'] = [1, 2, 3]
        # db.model.save(entry)
        return make_response(jsonify(labels), 200)


@app.route('/images', methods=['GET'])
def get_image_stats():
    if request.method == 'GET':
        stats = labelservice.count_images_for_all_labels(labels)
        return make_response(jsonify(stats), 200)


@app.route('/test', methods=['POST'])
def test():
    if request.method == 'POST':
        image = request.files['file']
        prediction = learningservice.test(image)
        return make_response(jsonify(labels[prediction[0]]), 200)


@app.route('/dev', methods=['GET'])
def empty_data_for_labels():
    if request.method == 'GET':
        devservice.empty_data_for_all_labels_in_db()
        return make_response(jsonify({'resp': 'testing'}), 200)


labels = ['cat', 'dog']
