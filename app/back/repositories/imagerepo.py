class ImageRepo:

    def __init__(self, db):
        self.db = db

    def save_image(self, label, data):
        entry = self.db.model.find_one({'label': label})
        if entry is None:
            self.db.model.insert({'label': label, 'images': []})
            entry = self.db.model.find_one({'label': label})
        data_array = [*data]
        entry['images'].append(data_array)
        self.db.model.save(entry)

    def get_all_images_for_label(self, label):
        return self.db.model.find_one({'label': label})['images']
