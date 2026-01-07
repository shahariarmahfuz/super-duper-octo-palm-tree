from flask import Blueprint, jsonify

from app.results.services import evaluate_attempt

results_bp = Blueprint("results", __name__, url_prefix="/results")


@results_bp.get("/<attempt_id>")
def view_result(attempt_id: str):
    return jsonify(evaluate_attempt(attempt_id))
