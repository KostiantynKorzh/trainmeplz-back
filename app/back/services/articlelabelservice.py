from app.back.db import articlelabelrepo


def get_label_by_id(id):
    return format_label(list(articlelabelrepo.get_label_by_id(id))[0])


def get_labels_by_ids(ids: list):
    labels = []
    if (ids):
        for id in ids:
            labels.append(get_label_by_id(id))

    return labels


def format_label(label):
    id = label['_id']
    del label['_id']
    label['id'] = str(id)

    return label


def get_all_labels():
    labels = list(articlelabelrepo.get_all_labels())
    for label in labels:
        format_label(label)

    return labels


def create_label(name):
    articlelabelrepo.create_label(name)
