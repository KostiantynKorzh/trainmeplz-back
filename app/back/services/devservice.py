from app.back import db
from app.back.services import labelservice


def empty_data_for_all_labels_in_db():
    labels = labelservice.get_all_labels()
    for label in labels:
        empty_data_for_label_in_db(label)


def empty_data_for_label_in_db(label):
    entry = db.model.find_one({'label': label})
    entry['images'] = []
    db.model.save(entry)
