import os


class Settings:
    APP_NAME = os.getenv('APP_NAME', 'Bika Marketplace')
    DB_NAME = os.getenv('DB_NAME', 'bika_bot')
    COIN_NAME = os.getenv('COIN_NAME', 'BKC')
    NFT_NAME = os.getenv('NFT_NAME', 'BIKA')
    MONGO_URL = os.getenv('MONGO_URL', 'mongodb://localhost:27017')
    ENV = os.getenv('ENV', 'development')
    JWT_SECRET = os.getenv('JWT_SECRET', 'change_me')
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', '*')


settings = Settings()
