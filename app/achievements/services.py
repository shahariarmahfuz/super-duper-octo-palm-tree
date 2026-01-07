from app.achievements.repository import fetch_achievement_history, fetch_badge_catalog
from app.achievements.validators import validate_user_achievement_request


def get_user_achievements(user_id: str) -> dict:
    validate_user_achievement_request(user_id)
    return {
        "achievements": fetch_achievement_history(user_id),
        "badges": fetch_badge_catalog(),
    }
