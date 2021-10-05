class LabelRepo:

    def __init__(self, db):
        self.db = db

    def get_all_labels(self):
        return self.db.stats.find({})

    def increment_image_count_for_label(self, label):
        label_stats = self.get_label_stats_by_label(label)
        if not label_stats:
            print('adding new label to label stats: {}'.format(label))
            self.db.stats.save({'label': label, 'images_count': 1})
            return
        label_stats['images_count'] += 1
        self.db.stats.save(label_stats)

    def get_label_stats_by_label(self, label):
        return self.db.stats.find_one({'label': label})
