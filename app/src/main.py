from flask import Flask
from errors import SharedPoolError

app = Flask(__name__)

from auth.routes import *


@app.errorhandler(SharedPoolError)
def handle_known_error(error):
    return error.to_flask_response()

if __name__ == '__main__':
    app.run()