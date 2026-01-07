from flask import Blueprint, jsonify

from app.achievements.services import get_user_achievements

achievements_bp = Blueprint("achievements", __name__, url_prefix="/achievements")


@achievements_bp.get("/users/<user_id>")
def user_achievements(user_id: str):
    return jsonify(get_user_achievements(user_id))
