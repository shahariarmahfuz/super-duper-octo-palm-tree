import os


class AppConfig:
    def __init__(self) -> None:
        self.APP_ENV = os.getenv("APP_ENV", "development")
        self.DATABASE_URL = os.getenv("DATABASE_URL")
        self.TURSO_AUTH_TOKEN = os.getenv("TURSO_AUTH_TOKEN")
        self.SESSION_SECRET = os.getenv("SESSION_SECRET")
        self.ADMIN_BOOTSTRAP_SECRET = os.getenv("ADMIN_BOOTSTRAP_SECRET")

        self.SECRET_KEY = self.SESSION_SECRET or "dev-secret-not-for-production"
        self._validate_required()

    def _validate_required(self) -> None:
        if self.APP_ENV != "production":
            return

        missing = [
            name
            for name, value in {
                "DATABASE_URL": self.DATABASE_URL,
                "TURSO_AUTH_TOKEN": self.TURSO_AUTH_TOKEN,
                "SESSION_SECRET": self.SESSION_SECRET,
            }.items()
            if not value
        ]
        if missing:
            raise RuntimeError(
                "Missing required environment variables: " + ", ".join(missing)
            )
