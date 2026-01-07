from app.admin.audit import record_audit_event


def bootstrap_admin():
    return None


def admin_health_status() -> dict:
    status = {"status": "ok"}
    record_audit_event("admin.healthcheck", status)
    return status
