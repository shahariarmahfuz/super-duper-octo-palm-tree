from flask import Blueprint, jsonify

from app.admin.services import admin_health_status

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


@admin_bp.get("/health")
def admin_health():
    return jsonify(admin_health_status())
