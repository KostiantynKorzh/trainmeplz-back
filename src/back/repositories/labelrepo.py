from src.back.setup import logger


class LabelRepo:

    def __init__(self, db):
        self.db = db

    def get_all_labels(self):
        logger.debug('Getting all labels')
        return self.db.stats.find({})

    def increment_image_count_for_label(self, label):
        label_stats = self.get_label_stats_by_label(label)
        if not label_stats:
            logger.debug('Adding new label to label stats: {}'.format(label))
            self.db.stats.save({'label': label, 'images_count': 1})
            return
        label_stats['images_count'] += 1
        self.db.stats.save(label_stats)

    def get_label_stats_by_label(self, label):
        logger.debug('Getting stats for label: {}'.format(label))
        return self.db.stats.find_one({'label': label})
