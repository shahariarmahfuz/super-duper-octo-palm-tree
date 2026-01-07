from flask import Blueprint, jsonify

exams_bp = Blueprint("exams", __name__, url_prefix="/exams")


@exams_bp.post("/start")
def start_exam():
    return jsonify({"status": "started"})
