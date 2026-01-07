from flask import Blueprint, jsonify

users_bp = Blueprint("users", __name__, url_prefix="/users")


@users_bp.get("/me")
def profile():
    return jsonify({"user": None})
