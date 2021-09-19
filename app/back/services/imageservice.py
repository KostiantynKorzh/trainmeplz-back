import cv2
import numpy as np

from app.back.db import db
from app.ml.services.dataservice import convert_image_to_array


def convert_image_to_data_and_save(image, label):
    try:
        nparr = np.fromstring(image.read(), np.uint8)
        img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        image_array = convert_image_to_array(img_np)
        save_image_data_with_label(image_array, label)
    except Exception as e:
        raise Exception(str(e))


def save_image_data_with_label(data, label):
    entry = db.model.find_one({'label': label})
    if entry is None:
        db.model.insert({'label': label, 'images': []})
        entry = db.model.find_one({'label': label})
    data_array = [*data]
    entry['images'].append(data_array)
    db.model.save(entry)
