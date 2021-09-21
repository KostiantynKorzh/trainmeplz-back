from app.back.db import labelrepo, imagerepo


def get_all_labels():
    labels = list(labelrepo.get_all_labels())
    return list(map(lambda x: x['label'], labels))


def count_images_for_all_labels(labels):
    stats = {}
    for label in labels:
        stats[label] = count_images_for_label(label)

    return stats


def count_images_for_label(label):
    images = imagerepo.get_all_images_for_label(label)
    return len(images)
