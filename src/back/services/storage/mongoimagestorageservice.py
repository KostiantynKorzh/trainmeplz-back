import gridfs

from src.back.services.storage.imagestorageservice import ImageStorageService
from src.back.services.storage.utils import create_labeled_filename
from src.back.setup import logger


class MongoImageStorageService(ImageStorageService):

    def __init__(self, db):
        super().__init__()
        self.fs = gridfs.GridFS(db)

    def save(self, image, label):
        try:
            filename = create_labeled_filename(label)
            self.fs.put(image.read(), filename=filename)
            logger.debug('Saving image to MongoDD with label: {}'.format(label))
        except Exception:
            logger.exception('Error during saving image to MongoDD with label: {}'.format(label))

    def get_filenames_for_all_files_with_label(self, label):
        pattern = label + '_'
        labeled_filenames = list(filter(lambda x: pattern in x, self.fs.list()))
        logger.debug('Getting filenames for all files with label: {}'.format(label))
        return labeled_filenames

    def delete_all_for_label(self, id):
        print('kek')

    def get_by_filename(self, filename):
        logger.debug('Getting file from MongoDB by filename: {}'.format(filename))
        return self.fs.find_one({'filename': filename}).read()
