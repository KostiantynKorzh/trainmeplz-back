from abc import abstractmethod, ABC

from src.back.setup import logger


class ImageStorageService(ABC):

    def __init__(self):
        logger.info('Initializing image service: {}'.format(self.__class__.__name__))

    @abstractmethod
    def save(self, image, label):
        raise Exception('should implement this method')

    @abstractmethod
    def get_filenames_for_all_files_with_label(self, label):
        raise Exception('should implement this method')

    @abstractmethod
    def delete_all_for_label(self, id):
        raise Exception('should implement this method')

    @abstractmethod
    def get_by_filename(self, filename):
        raise Exception('should implement this method')
