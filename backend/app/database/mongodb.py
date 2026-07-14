from motor.motor_asyncio import AsyncIOMotorClient
import os

client = AsyncIOMotorClient(os.getenv('MONGODB_URL','mongodb://localhost:27017'))
db = client['bika_bot']

# Existing Bika bot collections are accessed safely.
# Marketplace collections will be added separately.
