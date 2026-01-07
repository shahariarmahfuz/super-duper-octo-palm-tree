from flask import Blueprint, jsonify

from app.leaderboards.services import (
    get_accuracy_leaderboard,
    get_consistency_leaderboard,
    get_global_leaderboard,
    get_subject_leaderboard,
    get_time_leaderboard,
)

leaderboards_bp = Blueprint("leaderboards", __name__, url_prefix="/leaderboards")


@leaderboards_bp.get("/global")
def global_leaderboard():
    return jsonify({"leaders": get_global_leaderboard()})


@leaderboards_bp.get("/subjects/<subject_id>")
def subject_leaderboard(subject_id: str):
    return jsonify({"leaders": get_subject_leaderboard(subject_id)})


@leaderboards_bp.get("/time/<period>")
def time_leaderboard(period: str):
    return jsonify({"leaders": get_time_leaderboard(period)})


@leaderboards_bp.get("/accuracy")
def accuracy_leaderboard():
    return jsonify({"leaders": get_accuracy_leaderboard()})


@leaderboards_bp.get("/consistency")
def consistency_leaderboard():
    return jsonify({"leaders": get_consistency_leaderboard()})
