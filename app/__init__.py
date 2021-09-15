import os

from flask_cors import CORS
from flask import Flask, request

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

app.config["IMAGE_UPLOADS"] = r"C:\Users\Kostiantyn_Korzh\Desktop\self_study\ml\trainmeplz\back\app\images\\"


@app.route('/', methods=['GET', 'POST', 'DELETE', 'PATCH'])
def upload_image():
    if request.method == 'GET':
        return '<h1>Just testing...</h1>'
    elif request.method == 'POST':
        try:
            label = request.args.get('label')
            image = request.files['file']
            filename_with_label = add_label_to_filename(image.filename, label)
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename_with_label))
            return 'Image ' + image.filename + ' labeled with ' + label + ' was saved'
        except Exception:
            return 'Some error occurred'


def add_label_to_filename(filename, label):
    splitted_filename = filename.split('.')
    return splitted_filename[0] + '_label_' + label + '.' + splitted_filename[1]
