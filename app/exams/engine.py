from typing import Iterable


def select_questions(question_pool: Iterable, limit: int) -> list:
    return list(question_pool)[:limit]
