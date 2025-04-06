import os
from flask import Flask
from .models import db

def create_app():
    # Point Flask to the root-level templates folder
    template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
    static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))

    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

    # Load configuration
    app.config.from_object('config')

    # Init DB
    db.init_app(app)

    # Register Blueprint
    from app.routes import main
    app.register_blueprint(main)

    return app
