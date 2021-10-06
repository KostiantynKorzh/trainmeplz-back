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


def change_log_level(level):
    if level.lower() == 'debug':
        level_code = 10
    elif level.lower() == 'warning':
        level_code = 30
    elif level.lower() == 'error':
        level_code = 40
    elif level.lower() == 'fatal' or level.lower() == 'critical':
        level_code = 50
    else:
        level_code = 20
        level = 'info'
    app.logger.info('Changing log level to {}'.format(level.upper()))
    app.logger.setLevel(level_code)
