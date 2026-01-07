from app.announcements.repository import fetch_announcement, fetch_announcements


def list_announcements() -> list[dict]:
    return fetch_announcements()


def get_announcement(announcement_id: str) -> dict | None:
    return fetch_announcement(announcement_id)
