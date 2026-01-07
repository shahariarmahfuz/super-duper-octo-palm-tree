from typing import Optional

from app.config import AppConfig


class Database:
    def __init__(self, config: Optional[AppConfig] = None) -> None:
        self.config = config or AppConfig()
        self._client = None

    def connect(self) -> None:
        if self._client is not None:
            return
        from libsql_client import create_client

        self._client = create_client(
            self.config.DATABASE_URL,
            auth_token=self.config.TURSO_AUTH_TOKEN,
        )

    @property
    def client(self):
        if self._client is None:
            self.connect()
        return self._client
