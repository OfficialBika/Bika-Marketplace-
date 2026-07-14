from contextlib import asynccontextmanager

from app.database.mongodb import client


@asynccontextmanager
async def mongo_transaction():
    session = await client.start_session()
    try:
        async with session.start_transaction():
            yield session
    finally:
        await session.end_session()
