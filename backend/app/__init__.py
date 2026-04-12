import os

from flask import Flask
from flask_cors import CORS

from app.modules.core import core_bp
from app.modules.teams import teams_bp
from app.modules.auth import auth_bp
from app.extensions import bcrypt


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.secret_key = os.getenv("FLASK_SESSION_KEY", "my-secret-key")
    bcrypt.init_app(app)

    app.register_blueprint(core_bp)
    app.register_blueprint(teams_bp)
    app.register_blueprint(auth_bp)

    return app