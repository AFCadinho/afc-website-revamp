from flask import Blueprint

core_bp = Blueprint("core", __name__, url_prefix="/api")

@core_bp.route("/")
def home():
    return "AFC Adinho V2!\nHello World"