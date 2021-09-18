import os
import re
from pathlib import Path

from app.constants import UPLOAD_PATH


def save_image(image, label):
    try:
        path_with_label = UPLOAD_PATH + r'\\' + label + r"\\"
        Path(path_with_label).mkdir(parents=True, exist_ok=True)
        formatted_image_name = format_image_name(label)
        image.save(os.path.join(path_with_label, formatted_image_name))
    except Exception as e:
        print(e)
        raise Exception('Problem during saving file...')


def format_image_name(label):
    path = UPLOAD_PATH.format(label)
    filenames = os.listdir(path)
    filenames.sort(key=lambda x: int(re.sub(r'\D+', '', x)))
    last_file_name = filenames[-1]
    last_index = re.sub(r'\D+', '', last_file_name)
    ext = re.sub(r'.*\.', '', last_file_name)
    return str(int(last_index) + 1) + '_' + label + '.' + ext
