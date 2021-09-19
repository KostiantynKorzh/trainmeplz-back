labels = ['cat', 'dog']

from app.back.application import app as application
import app.back.routing

from app.back.constants import UPLOAD_PATH

if __name__ == "__main__":
    application.run(debug=True)
