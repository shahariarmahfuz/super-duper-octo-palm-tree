from app.subjects.repository import fetch_subjects


def list_all_subjects() -> list[dict]:
    return fetch_subjects()
