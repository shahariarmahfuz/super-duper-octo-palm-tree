from app.mcqs.mapper import normalize_mcq_payload
from app.mcqs.repository import fetch_mcqs


def list_all_mcqs() -> list[dict]:
    mcqs = fetch_mcqs()
    return [normalize_mcq_payload(mcq) for mcq in mcqs]
