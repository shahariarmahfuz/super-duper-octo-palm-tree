from app.users.repository import fetch_profile, fetch_public_profile
from app.users.validators import validate_profile_request


def get_profile(user_id: str) -> dict | None:
    validate_profile_request(user_id)
    return fetch_profile(user_id)


def get_public_profile(user_id: str) -> dict | None:
    validate_profile_request(user_id)
    return fetch_public_profile(user_id)
