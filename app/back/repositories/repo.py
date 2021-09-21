class Repo:

    def __init__(self, db):
        self.db = db

    def clear_all(self):
        self.db.model.remove({})

    def clear_images_for_label(self, label):
        entry = self.db.model.find_one({'label': label})
        entry['images'] = []
        self.db.model.save(entry)
