from app.back.db import imagestorageservice
from app.back.services import labelservice


def save_image(image, label):
    imagestorageservice.save(image, label)
    labelservice.add_to_label_stats(label)


def get_image_by_filename(filename):
    imagestorageservice.get_by_filename(filename)


def get_all_images_for_label(label):
    return imagestorageservice.get_filenames_for_all_files_with_label(label)
