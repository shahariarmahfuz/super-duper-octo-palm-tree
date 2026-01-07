def validate_period(period: str) -> bool:
    return period in {"daily", "weekly", "monthly"}


def validate_subject_leaderboard(subject_id: str) -> bool:
    return bool(subject_id)
