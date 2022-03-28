from flask import Blueprint
from controllers.apiController import *

apiRoute = Blueprint('apiRoute', __name__)
apiRoute.route('/', methods=['GET'])(index)
apiRoute.route('/datetime', methods=['GET'])(getDateTime)
apiRoute.route('/audio', methods=['POST'])(postAudio)
