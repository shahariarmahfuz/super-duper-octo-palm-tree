from app.auth.repository import get_user_by_email
from app.auth.validators import validate_login_payload


def authenticate_user():
    payload = validate_login_payload()
    return get_user_by_email(payload["email"])
