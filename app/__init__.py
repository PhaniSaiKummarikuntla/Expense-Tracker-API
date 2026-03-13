from flask import Flask
from .routes import routes
from .database import init_db

def create_app():

    app = Flask(__name__)

    init_db()

    app.register_blueprint(routes)

    return app