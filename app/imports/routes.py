from flask import Blueprint, jsonify, request

from app.imports.services import create_import_request

imports_bp = Blueprint("imports", __name__, url_prefix="/imports")


@imports_bp.post("/")
def create_import():
    payload = request.get_json(silent=True) or {}
    return jsonify(create_import_request(payload)), 202
