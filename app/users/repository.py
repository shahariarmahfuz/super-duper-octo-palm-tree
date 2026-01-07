def fetch_profile(user_id: str) -> dict:
    return {"id": user_id, "summary": {}, "strengths": [], "weaknesses": []}


def fetch_public_profile(user_id: str) -> dict:
    return {"id": user_id, "display_name": "Learner", "rank_history": []}
