import os

from app.back import UPLOAD_PATH


def add_label_to_filename(filename, label):
    splitted_filename = filename.split('.')
    return splitted_filename[0] + '_label_' + label + '.' + splitted_filename[1]


def save_image(image, label):
    try:
        filename_with_label = add_label_to_filename(image.filename, label)
        image.save(os.path.join(UPLOAD_PATH, filename_with_label))
    except Exception:
        raise Exception('Problem during saving file...')
