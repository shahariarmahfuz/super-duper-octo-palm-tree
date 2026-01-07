from flask import Blueprint, jsonify, request

from app.exams.services import start_exam_session

exams_bp = Blueprint("exams", __name__, url_prefix="/exams")


@exams_bp.post("/start")
def start_exam():
    payload = request.get_json(silent=True) or {}
    return jsonify(start_exam_session(payload))
