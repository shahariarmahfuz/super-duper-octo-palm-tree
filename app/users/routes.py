from flask import Blueprint, jsonify

from app.users.services import get_profile, get_public_profile

users_bp = Blueprint("users", __name__, url_prefix="/users")


@users_bp.get("/me")
def profile():
    return jsonify({"user": get_profile("me")})


@users_bp.get("/<user_id>/public")
def public_profile(user_id: str):
    return jsonify({"user": get_public_profile(user_id)})
