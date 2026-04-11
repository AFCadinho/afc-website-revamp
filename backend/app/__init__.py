from flask import Flask
from flask_cors import CORS

from app.modules.core import core_bp
from app.modules.teams import teams_bp


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(core_bp)
    app.register_blueprint(teams_bp)

    return app