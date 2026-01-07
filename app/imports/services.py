from app.imports.batch import summarize_batch
from app.imports.repository import create_import_batch
from app.imports.validators import validate_import_payload


def create_import_request(payload: dict | None = None) -> dict:
    payload = payload or {}
    validate_import_payload(payload)
    batch = create_import_batch()
    return summarize_batch(batch.get("imported", 0), batch.get("errors", []))
