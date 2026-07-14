import os

class Settings:
    APP_NAME = os.getenv('APP_NAME','Bika Marketplace')
    MONGO_URL = os.getenv('MONGO_URL','mongodb://localhost:27017')
    DB_NAME = os.getenv('DB_NAME','bika_bot')
    COIN_NAME = os.getenv('COIN_NAME','BKC')
    ENV = os.getenv('ENV','development')

settings = Settings()
