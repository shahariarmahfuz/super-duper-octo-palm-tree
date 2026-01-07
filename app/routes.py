from flask import Blueprint, jsonify

core_bp = Blueprint("core", __name__)


@core_bp.get("/health")
def healthcheck():
    return jsonify({"status": "ok"})
