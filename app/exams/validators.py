def validate_exam_request(payload: dict) -> bool:
    return isinstance(payload, dict)
