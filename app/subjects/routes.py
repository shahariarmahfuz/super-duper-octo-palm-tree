from flask import Blueprint, jsonify

subjects_bp = Blueprint("subjects", __name__, url_prefix="/subjects")


@subjects_bp.get("/")
def list_subjects():
    return jsonify({"subjects": []})
