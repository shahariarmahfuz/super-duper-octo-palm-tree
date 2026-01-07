from flask import Blueprint, jsonify

results_bp = Blueprint("results", __name__, url_prefix="/results")


@results_bp.get("/<attempt_id>")
def view_result(attempt_id: str):
    return jsonify({"attempt": attempt_id})
