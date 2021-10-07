import re
import uuid


def get_label_from_filename(filename):
    return re.sub(r'_.*', '', filename)


def create_labeled_filename(label):
    return label + '_' + str(uuid.uuid4())
