from app.roles.policies import can_manage_roles
from app.roles.repository import fetch_role_catalog


def list_roles(user: dict | None = None) -> list[dict]:
    can_manage_roles(user)
    return fetch_role_catalog()
