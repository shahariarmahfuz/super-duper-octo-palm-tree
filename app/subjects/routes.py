from flask import Blueprint, jsonify

from app.subjects.services import list_all_subjects

subjects_bp = Blueprint("subjects", __name__, url_prefix="/subjects")

@subjects_bp.get("/")
def list_subjects():
    return jsonify({"subjects": list_all_subjects()})
