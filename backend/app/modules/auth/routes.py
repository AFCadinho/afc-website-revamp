from flask import Blueprint, request, jsonify, session as flask_session
from database.database import Session
from sqlalchemy import select
from database.models import User
from app.extensions import bcrypt

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or {}

    name = data.get("name", "").strip()
    password = data.get("password", "")

    if not name or not password:
        return jsonify({"error": "Name and password are mandatory"}), 400
    
    with Session.begin() as db_session:
        stmt = select(User).where(User.name == name)
        user = db_session.scalar(stmt)

        if not user:
            return jsonify({"error": "Invalid login"}), 401
        
        if not bcrypt.check_password_hash(user.password, password):
            return jsonify({"error": "Invalid login"}), 401
        
        if user.is_banned:
            return jsonify({"error": "Account is blocked"}), 403

        flask_session.clear()
        flask_session["user_id"] = user.id

        user_data = {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "is_admin": user.is_admin
        }
    
    return jsonify({
        "message": "Login successful",
        "user": user_data
    }), 200


@auth_bp.route("/logout", methods=["POST"])
def logout():
    flask_session.clear()
    return jsonify({"message": "Logged out"}), 200