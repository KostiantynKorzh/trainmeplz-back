import cv2
import numpy as np

from app.ml.services.dataservice import convert_image_to_array
from app.ml.services.learningservice import Model


def test(image):
    nparr = np.fromstring(image.read(), np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    image_array = convert_image_to_array(img_np)
    data = {'data': image_array, 'target': [0, ]}

    model = Model('cat', 'dog')
    model.train()
    print(data)

    return model.test(data)
