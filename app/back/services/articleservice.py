from app.back.db import articlerepo
from app.back.services import articlelabelservice


def get_all_articles():
    articles = list(articlerepo.get_all_articles())
    for article in articles:
        format_labels_for_article(article)

    return articles


def format_labels_for_article(article):
    raw_labels = article['labelsIds']
    formatted_labels = articlelabelservice.get_labels_by_ids(raw_labels)
    del article['labelsIds']
    id = article['_id']
    article['labels'] = formatted_labels
    del article['_id']
    article['id'] = str(id)


def create_article(title, description, content, labels):
    articlerepo.create_article(title, description, content, labels)
