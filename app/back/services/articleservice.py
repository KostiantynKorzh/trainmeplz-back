from app.back.db import articlerepo
from app.back.services import articlelabelservice


def get_all_articles():
    articles = list(articlerepo.get_all_articles())
    for article in articles:
        format_labels_for_article(article)

    return articles


def get_article_by_id(id):
    article = list(articlerepo.get_article_by_id(id))[0]
    format_labels_for_article(article)
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


def create_article(title, description, content, labels):
    articlerepo.create_article(title, description, content, labels)


def update_article(id, title, description, content, labels):
    articlerepo.update_article(id, title, description, content, labels)


def delete_article(id):
    articlerepo.delete_article(id)
