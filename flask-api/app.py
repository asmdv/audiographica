from flask import Flask
from flask_cors import CORS
from routes.apiRoute import apiRoute
import logging
app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('HELLO WORLD')

app.register_blueprint(apiRoute, url_prefix='/api')

@app.route("/")
def index():
    return "Your app is running! Refer to /api"

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)