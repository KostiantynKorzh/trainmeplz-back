from src.back.repositories import labelrepo
from src.back.setup import logger


def get_all_labels():
    logger.debug('Getting all labels')
    return list(map(lambda x: x['label'], list(labelrepo.get_all_labels())))


def add_to_label_stats(label):
    labelrepo.increment_image_count_for_label(label)
    logger.debug('Incrementing image count for {}'.format(label))


def get_stats_for_all_labels():
    stats = {}
    labels = get_all_labels()
    for label in labels:
        stats[label] = get_stats_for_label(label)

    logger.debug('Getting stats for all labels')
    return stats


def get_stats_for_label(label):
    logger.debug('Getting stats for {}'.format(label))
    return labelrepo.get_label_stats_by_label(label)['images_count']
