import os

from app.constants import UPLOAD_PATH


def get_all_labels():
    return ['cat', 'dog']


def count_images_for_all_labels(labels):
    stats = {}
    for label in labels:
        stats[label] = count_images_for_label(label)

    return stats


def count_images_for_label(label):
    path = UPLOAD_PATH.format(label)
    return len(os.listdir(path))
