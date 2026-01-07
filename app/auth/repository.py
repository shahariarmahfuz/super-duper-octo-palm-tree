from typing import Dict, Optional


def get_user_by_email(email: str) -> Optional[Dict[str, str]]:
    return {"email": email}
