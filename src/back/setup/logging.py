import logging


def setup_logging(app):
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)s %(threadName)s %(pathname)s : %(message)s')
    logger = app.logger
    return logger
