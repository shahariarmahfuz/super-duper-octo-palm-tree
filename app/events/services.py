from app.events.repository import fetch_event, fetch_scheduled_events


def list_scheduled_events() -> list[dict]:
    return fetch_scheduled_events()


def get_event(event_id: str) -> dict | None:
    return fetch_event(event_id)
