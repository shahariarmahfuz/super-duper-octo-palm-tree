from flask import Blueprint, jsonify

from app.events.services import get_event, list_scheduled_events

events_bp = Blueprint("events", __name__, url_prefix="/events")


@events_bp.get("/")
def events_index():
    return jsonify({"events": list_scheduled_events()})


@events_bp.get("/<event_id>")
def event_detail(event_id: str):
    return jsonify({"event": get_event(event_id)})
