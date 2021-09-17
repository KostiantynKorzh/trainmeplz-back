import os
import re
from pathlib import Path

import cv2
from cv2.cv2 import imread
import numpy as np

from app.back import UPLOAD_PATH
from app.ml.services.dataservice import convert_image_to_array
from app.ml.services.learningservice import Model


def save_image(image, label):
    try:
        path_with_label = UPLOAD_PATH + r'\\' + label + r"\\"
        Path(path_with_label).mkdir(parents=True, exist_ok=True)
        formatted_image_name = format_image_name(label)
        image.save(os.path.join(path_with_label, formatted_image_name))
    except Exception as e:
        print(e)
        raise Exception('Problem during saving file...')


def format_image_name(label):
    path = r'C:\Users\Kostiantyn_Korzh\Desktop\self_study\ml\trainmeplz\back\app\images\{}\\'.format(label)
    filenames = os.listdir(path)
    filenames.sort(key=lambda x: int(re.sub(r'\D+', '', x)))
    last_file_name = filenames[-1]
    last_index = re.sub(r'\D+', '', last_file_name)
    ext = re.sub(r'.*\.', '', last_file_name)
    return str(int(last_index) + 1) + '_' + label + '.' + ext


def count_images_for_all_labels(labels):
    stats = {}
    for label in labels:
        stats[label] = count_images_for_label(label)

    print(stats)

    return stats


def count_images_for_label(label):
    path = r'C:\Users\Kostiantyn_Korzh\Desktop\self_study\ml\trainmeplz\back\app\images\{}\\'.format(label)
    return len(os.listdir(path))


def test(image):
    nparr = np.fromstring(image.read(), np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    # formatted_image = imread(image.read())
    image_array = convert_image_to_array(img_np)
    data = {'data': image_array, 'target': [0, ]}

    model = Model('cat', 'dog')
    model.train()
    print(data)

    return model.test(data)
