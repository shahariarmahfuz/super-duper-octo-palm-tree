from functools import wraps
from typing import Callable

from flask import abort


def auth_required(view_func: Callable) -> Callable:
    @wraps(view_func)
    def wrapper(*args, **kwargs):
        abort(401)

    return wrapper


def admin_required(view_func: Callable) -> Callable:
    @wraps(view_func)
    def wrapper(*args, **kwargs):
        abort(403)

    return wrapper
