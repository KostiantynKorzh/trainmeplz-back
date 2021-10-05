from app.back.db import repo
from app.back.services import labelservice


def empty_all():
    repo.clear_all()


def empty_data_for_all_labels_in_db():
    labels = labelservice.get_all_labels()
    for label in labels:
        empty_data_for_label_in_db(label)


def empty_data_for_label_in_db(label):
    repo.clear_images_for_label(label)

def empty_stats_for_label(label):
    repo.clear_stats_for_label(label)
