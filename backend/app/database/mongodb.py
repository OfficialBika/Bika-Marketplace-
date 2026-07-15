import os
from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient(os.getenv("MONGO_URL", ""))
db = client[os.getenv("MONGO_DB", "bika_marketplace")]
