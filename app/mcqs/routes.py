from flask import Blueprint, jsonify

mcqs_bp = Blueprint("mcqs", __name__, url_prefix="/mcqs")


@mcqs_bp.get("/")
def list_mcqs():
    return jsonify({"mcqs": []})
