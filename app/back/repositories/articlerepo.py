class ArticleRepo:

    def __init__(self, db):
        self.db = db

    def get_all_articles(self):
        return self.db.articles.find({})

    def create_article(self, title, description, content, labelsIds):
        self.db.articles.save({'title': title, 'description': description, 'content': content, 'labelsIds': labelsIds})
