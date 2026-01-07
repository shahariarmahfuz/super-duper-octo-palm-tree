from flask import Blueprint, jsonify

imports_bp = Blueprint("imports", __name__, url_prefix="/imports")


@imports_bp.post("/")
def create_import():
    return jsonify({"status": "accepted"})
