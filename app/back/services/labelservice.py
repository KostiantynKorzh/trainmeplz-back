from app.back.db import labelrepo

def get_all_labels():
    # return list(map(lambda x: x['label'], list(labelrepo.get_all_labels())))
    return ['cat', 'dog']


def add_to_label_stats(label):
    labelrepo.increment_image_count_for_label(label)


def get_stats_for_all_labels():
    stats = {}
    labels = get_all_labels()
    for label in labels:
        stats[label] = get_stats_for_label(label)

    return stats


def get_stats_for_label(label):
    return labelrepo.get_label_stats_by_label(label)['images_count']
