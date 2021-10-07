from src.back.repositories.articlelabelrepo import ArticleLabelRepo
from src.back.repositories.articlerepo import ArticleRepo
from src.back.repositories.imagerepo import ImageRepo
from src.back.repositories.labelrepo import LabelRepo
from src.back.repositories.repo import Repo
from src.back.setup import dataset_db, article_db

labelrepo = LabelRepo(dataset_db)
imagerepo = ImageRepo(dataset_db, None)
repo = Repo(dataset_db)
articlerepo = ArticleRepo(article_db)
articlelabelrepo = ArticleLabelRepo(article_db)