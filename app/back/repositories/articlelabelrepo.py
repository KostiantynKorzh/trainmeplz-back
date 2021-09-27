from bson import ObjectId


class ArticleLabelRepo:

    def __init__(self, db):
        self.db = db

    def get_all_labels(self):
        return self.db.labels.find({})

    def get_label_by_id(self, id):
        return self.db.labels.find({'_id': ObjectId(id)})

    def create_label(self, name):
        self.db.labels.save({'name': name})
