def fetch_role_catalog() -> list[dict]:
    return [
        {"id": "super-admin", "name": "Super Admin"},
        {"id": "institution-admin", "name": "Institution Admin"},
        {"id": "content-manager", "name": "Content Manager"},
        {"id": "reviewer", "name": "Reviewer"},
        {"id": "instructor", "name": "Instructor"},
    ]
