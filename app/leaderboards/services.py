from app.leaderboards.policies import can_view_leaderboards
from app.leaderboards.repository import (
    fetch_accuracy_leaderboard,
    fetch_consistency_leaderboard,
    fetch_global_leaderboard,
    fetch_subject_leaderboard,
    fetch_time_leaderboard,
)
from app.leaderboards.validators import validate_period, validate_subject_leaderboard


def get_global_leaderboard(user: dict | None = None) -> list[dict]:
    can_view_leaderboards(user)
    return fetch_global_leaderboard()


def get_subject_leaderboard(subject_id: str, user: dict | None = None) -> list[dict]:
    validate_subject_leaderboard(subject_id)
    can_view_leaderboards(user)
    return fetch_subject_leaderboard(subject_id)


def get_time_leaderboard(period: str, user: dict | None = None) -> list[dict]:
    validate_period(period)
    can_view_leaderboards(user)
    return fetch_time_leaderboard(period)


def get_accuracy_leaderboard(user: dict | None = None) -> list[dict]:
    can_view_leaderboards(user)
    return fetch_accuracy_leaderboard()


def get_consistency_leaderboard(user: dict | None = None) -> list[dict]:
    can_view_leaderboards(user)
    return fetch_consistency_leaderboard()
