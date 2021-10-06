from app.back.application import app
from app.back.db import repo
from app.back.services import labelservice


def empty_all():
    repo.clear_all()
    app.logger.info('Clearing all info in db')


def empty_data_for_all_labels_in_db():
    labels = labelservice.get_all_labels()
    for label in labels:
        empty_data_for_label_in_db(label)
    app.logger.info('Clearing data for all labels in db')


def empty_data_for_label_in_db(label):
    repo.clear_images_for_label(label)
    app.logger.info('Clearing data for label {}'.format(label))


def empty_stats_for_label(label):
    repo.clear_stats_for_label(label)
    app.logger.info('Clearing stats for label {}'.format(label))
