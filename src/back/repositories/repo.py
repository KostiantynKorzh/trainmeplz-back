import gridfs

from src.back.services import imageservice
from src.back.setup import logger


class Repo:

    def __init__(self, db):
        self.db = db
        self.fs = gridfs.GridFS(db)

    def clear_all(self):
        self.db.fs.chunks.remove({})
        self.db.fs.files.remove({})
        self.clear_stats_for_all()

    def clear_images_for_label(self, label):
        try:
            labeled_filenames = imageservice.get_all_images_for_label(label)
            for filename in labeled_filenames:
                entry = self.fs.find_one({'filename': filename})
                self.fs.delete(entry._id)
        except Exception as e:
            logger.warning('Getting stats for label: {}'.format(label))

    def clear_stats_for_label(self, label):
        entry = self.db.stats.find_one({'label': label})
        entry['images_count'] = 0
        self.db.stats.save(entry)

    def clear_stats_for_all(self):
        stats = self.db.stats.find({})
        for stat in stats:
            self.clear_stats_for_label(stat['label'])
