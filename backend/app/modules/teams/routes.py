from flask import Blueprint, jsonify

teams_bp = Blueprint("teams", __name__, url_prefix="/api/teams")

@teams_bp.route("/")
def get_teams():
    return jsonify([
        {"id": 1, "name": "Rain Team"},
        {"id": 2, "name": "Sun Team"},
    ])