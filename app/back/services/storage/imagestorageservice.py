class ImageStorageService:

    def save(self, image, label):
        raise Exception('should implement this method')

    def get_all_for_label(self, label):
        raise Exception('should implement this method')

    def delete_all_for_label(self, id):
        raise Exception('should implement this method')
