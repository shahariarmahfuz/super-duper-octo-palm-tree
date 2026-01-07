from flask import Blueprint, jsonify

from app.mcqs.services import list_all_mcqs

mcqs_bp = Blueprint("mcqs", __name__, url_prefix="/mcqs")

@mcqs_bp.get("/")
def list_mcqs():
    return jsonify({"mcqs": list_all_mcqs()})
