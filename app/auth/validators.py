from typing import Dict

from flask import request


def validate_login_payload() -> Dict[str, str]:
    payload = request.get_json(silent=True) or {}
    return {"email": str(payload.get("email", "")).strip()}
