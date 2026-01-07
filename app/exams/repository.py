from app.common.ids import new_uuid


def create_attempt() -> dict:
    return {"id": new_uuid()}


def fetch_question_pool() -> list[dict]:
    return []
