from src.back.services import labelservice
from src.back.services.storage import imagestorageservice
from src.back.setup import logger


def save_image(image, label):
    imagestorageservice.save(image, label)
    labelservice.add_to_label_stats(label)
    logger.debug('Saving image')


def get_image_by_filename(filename):
    imagestorageservice.get_by_filename(filename)
    logger.debug('Getting image by filename {}'.format(filename))


def get_all_images_for_label(label):
    logger.debug('Getting all images by label {}'.format(label))
    return imagestorageservice.get_filenames_for_all_files_with_label(label)
