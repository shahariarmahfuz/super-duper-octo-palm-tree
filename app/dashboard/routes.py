from flask import Blueprint, jsonify

from app.dashboard.services import build_dashboard_snapshot

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")


@dashboard_bp.get("/")
def dashboard_home():
    return jsonify(build_dashboard_snapshot())
