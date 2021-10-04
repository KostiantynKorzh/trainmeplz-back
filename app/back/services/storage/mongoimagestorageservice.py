import uuid

import gridfs

from app.back.services.storage.imagestorageservice import ImageStorageService
from app.back.services.storage.utils import create_labeled_filename


class MongoImageStorageService(ImageStorageService):

    def __init__(self, db):
        self.fs = gridfs.GridFS(db)

    def save(self, image, label):
        try:
            filename = create_labeled_filename(label)
            print(filename)
            image = self.fs.put(image.read(), filename=filename)
            print(self.fs.get(image).read())
        except Exception as e:
            print(str(e))

    def get_filenames_for_all_files_with_label(self, label):
        pattern = label + '_'
        labeled_filenames = list(filter(lambda x: pattern in x, self.fs.list()))
        return labeled_filenames

    def delete_all_for_label(self, id):
        print('kek')

    def get_by_filename(self, filename):
        return self.fs.find_one({'filename': filename}).read()
