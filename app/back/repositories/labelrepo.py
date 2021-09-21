class LabelRepo:

    def __init__(self, db):
        self.db = db

    def get_all_labels(self):
        return self.db.model.find({}, {'label': 1, '_id': 0})
