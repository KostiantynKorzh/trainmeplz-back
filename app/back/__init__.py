from app.back.resources.dev import Dev
from app.back.resources.stats.images import ImageStats
from app.back.resources.stats.stats import Stats
from app.back.resources.tests import Test
from app.back.resources.trains import Train
from app.back.resources.labels import Label

from app.back.application import docs

from app.back.application import app as application
import app.back.routing

from app.back.constants import UPLOAD_PATH

# docs.register(Stats)
# # docs.register(ImageStats)
# docs.register(Dev)
# docs.register(Label)
# docs.register(Test)
# docs.register(Train)

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000, debug=True)
