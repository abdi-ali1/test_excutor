import os


class Settings:
    def __init__(self) -> None:
        self.redis_broker_url: str = os.getenv("REDIS_BROKER_URL", "redis://localhost:6379/0")
        self.redis_result_backend: str = os.getenv("REDIS_RESULT_BACKEND", "redis://localhost:6379/1")


settings = Settings()
