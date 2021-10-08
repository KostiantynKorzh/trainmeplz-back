from src.back.repositories import articlerepo
from src.back.services import articlelabelservice
from src.back.setup import logger


def get_all_articles():
    articles = list(articlerepo.get_all_articles())
    print(articles)
    for article in articles:
        format_labels_for_article(article)

    logger.debug('Getting all articles')
    return articles


def get_article_by_id(id):
    article = list(articlerepo.get_article_by_id(id))[0]
    format_labels_for_article(article)
    logger.debug('Getting article with id: {}'.format(id))
    return article


def format_labels_for_article(article):
    if 'labelsIds' in article:
        raw_labels = article['labelsIds']
        formatted_labels = articlelabelservice.get_labels_by_ids(raw_labels)
        del article['labelsIds']
        id = article['_id']
        article['labels'] = formatted_labels
        del article['_id']
        article['id'] = str(id)
        logger.debug('Formatting label for article: {}'.format(article['id']))


def create_article(title, description, content, labels):
    if not labels:
        labels = []
    articlerepo.create_article(title, description, content, labels)
    logger.info('Creating article with title: {}'.format(title))


def update_article(id, title, description, content, labels):
    articlerepo.update_article(id, title, description, content, labels)
    logger.info('Updating article with id: {} and title: {}'.format(id, title))


def delete_article(id):
    articlerepo.delete_article(id)
    logger.info('Deleting article with id: {}'.format(id))
