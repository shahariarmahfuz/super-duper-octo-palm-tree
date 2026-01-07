from flask import Blueprint, jsonify

from app.dashboard.aggregators import summarize_dashboard

dashboard_bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")


@dashboard_bp.get("/")
def dashboard_home():
    return jsonify(summarize_dashboard())
