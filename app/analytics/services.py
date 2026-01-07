from app.analytics.repository import (
    fetch_cohort_comparison,
    fetch_growth_trends,
    fetch_question_difficulty,
    fetch_subject_performance,
)


def build_subject_analysis() -> list[dict]:
    return fetch_subject_performance()


def build_question_analysis() -> list[dict]:
    return fetch_question_difficulty()


def build_cohort_analysis() -> list[dict]:
    return fetch_cohort_comparison()


def build_growth_trends() -> list[dict]:
    return fetch_growth_trends()
