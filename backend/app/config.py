import os

class Settings:
    MONGO_URL = os.getenv("MONGO_URL", "")
    JWT_SECRET = os.getenv("JWT_SECRET", "")
    SHOW_RARITY = os.getenv("SHOW_RARITY", "Supreme")
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*")

settings = Settings()
