from src.back.setup.db import setup_db
from src.back.setup.application import create_app
from src.back.setup.logging import setup_logging

app = create_app()
logger = setup_logging(app)

dataset_db, article_db = db.setup_db(app)
