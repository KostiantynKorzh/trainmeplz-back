import cv2
import numpy as np

from app.back.db import imagerepo
from app.ml.services.dataservice import convert_image_to_array


def convert_image_to_data_and_save(image, label):
    try:
        data = convert_image_to_data(image)
        imagerepo.save_image(label, data)
    except Exception as e:
        raise Exception(str(e))


def convert_image_to_data(image):
    nparr = np.fromstring(image.read(), np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return convert_image_to_array(img_np)
