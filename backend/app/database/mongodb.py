from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_URL = os.getenv('MONGODB_URL', os.getenv('MONGO_URL', 'mongodb://localhost:27017'))
DB_NAME = os.getenv('DB_NAME', 'bika_bot')

client = AsyncIOMotorClient(MONGO_URL)
db = client[DB_NAME]


async def check_connection():
    await client.admin.command('ping')
    return True


# Existing Bika bot collections remain untouched.
# Marketplace collections are managed separately.
