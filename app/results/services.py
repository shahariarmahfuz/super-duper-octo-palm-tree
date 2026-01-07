from app.results.evaluators import score_answers
from app.results.repository import fetch_attempt


def evaluate_attempt(attempt_id: str) -> dict:
    attempt = fetch_attempt(attempt_id)
    score = score_answers(attempt.get("answers", []))
    return {"attempt": attempt, "score": score}
