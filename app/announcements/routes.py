from flask import Blueprint, jsonify

from app.announcements.services import get_announcement, list_announcements

announcements_bp = Blueprint("announcements", __name__, url_prefix="/announcements")


@announcements_bp.get("/")
def announcements_index():
    return jsonify({"announcements": list_announcements()})


@announcements_bp.get("/<announcement_id>")
def announcement_detail(announcement_id: str):
    return jsonify({"announcement": get_announcement(announcement_id)})
