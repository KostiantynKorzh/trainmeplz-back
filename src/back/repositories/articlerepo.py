from bson import ObjectId


class ArticleRepo:

    def __init__(self, db):
        self.db = db

    def get_article_by_id(self, id):
        return self.db.articles.find({'_id': ObjectId(id)})

    def get_all_articles(self):
        return self.db.articles.find({})

    def create_article(self, title, description, content, labels_ids):
        self.db.articles.save({'title': title, 'description': description, 'content': content, 'labelsIds': labels_ids})

    def update_article(self, id, title, description, content, labels_ids):
        article = list(self.get_article_by_id(id))[0]
        article['title'] = title
        article['description'] = description
        article['content'] = content
        article['labelsIds'] = labels_ids
        self.db.articles.save(article)

    def delete_article(self, id):
        self.db.articles.remove({'_id': ObjectId(id)})
