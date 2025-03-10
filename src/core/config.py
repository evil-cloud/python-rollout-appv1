import os

class Settings:
    PROJECT_NAME: str = "Rollout Service"
    VERSION: str = "1.0.3"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:////app/data/database.db")

settings = Settings()
