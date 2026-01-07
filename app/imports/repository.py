from app.common.ids import new_uuid


def create_import_batch() -> dict:
    return {"id": new_uuid(), "imported": 0, "errors": []}
