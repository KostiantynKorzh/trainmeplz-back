from src.back.setup import app
from src.back.setup import routing
from src.back.setup import swagger

routing.setup_routing(app)
swagger.setup_swagger(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
