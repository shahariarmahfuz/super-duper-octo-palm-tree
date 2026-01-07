from app.exams.engine import select_questions
from app.exams.repository import create_attempt, fetch_question_pool
from app.exams.validators import validate_exam_request


def start_exam_session(payload: dict | None = None) -> dict:
    validate_exam_request(payload or {})
    questions = fetch_question_pool()
    selected_questions = select_questions(questions, limit=10)
    attempt = create_attempt()
    return {"attempt": attempt, "questions": selected_questions}
