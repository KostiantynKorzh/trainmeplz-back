import os

import numpy as np
from skimage.io import imread

from app.constants import UPLOAD_PATH
from app.ml.services.imageservice import resize_image


def create_dataset_for_labels(labels):
    dataset = {'target': [], 'target_names': []}
    label_code = 0
    data = []

    for label in labels:
        data_for_label = convert_all_images_to_array(label)
        data.extend(data_for_label)
        for _ in data_for_label:
            dataset['target'].append(label_code)
        label_code += 1
        dataset['target_names'].append(label)

    dataset['data'] = data

    return dataset


def convert_all_images_to_array(label):
    files = get_files_for_label(label)
    dataset = []
    for image in files:
        print('Processing image ' + image)
        feature_matrix = convert_saved_image_to_array(label, image)
        dataset.append(feature_matrix)

    return dataset


def convert_saved_image_to_array(label, image_name):
    image = imread(UPLOAD_PATH + r'{}\{}\\'
                   .format(label, image_name))
    return convert_image_to_array(image)


def convert_image_to_array(image):
    formatted_image = resize_image(image)
    height = formatted_image.shape[0]
    width = formatted_image.shape[1]
    feature_matrix = np.zeros(height * width, dtype=float)

    k = 0
    for i in range(0, height):
        for j in range(0, width):
            r_value = int(formatted_image[i, j, 0])
            g_value = int(formatted_image[i, j, 1])
            b_value = int(formatted_image[i, j, 2])
            feature_matrix[k] = (r_value + g_value + b_value) / 3
            k += 1

    return feature_matrix


def get_files_for_label(label):
    path = r'C:\Users\Kostiantyn_Korzh\Desktop\self_study\ml\trainmeplz\back\app\images\{}\\'.format(label)
    return os.listdir(path)
