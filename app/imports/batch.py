def summarize_batch(imported_count: int, errors: list[str]) -> dict:
    return {"imported": imported_count, "errors": errors}
