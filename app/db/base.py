"""AsyncMongoDBSession
Async MongoDB Session Manager
"""

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from app.core.config import settings


class AsyncMongoDBSession:
    def __init__(self):
        self._client: AsyncIOMotorClient = None
        self._database: AsyncIOMotorDatabase = None

    async def init(self):
        """Initializing MongoDB"""
        self._client = AsyncIOMotorClient(settings.DATABASE_URL)
        self._database = self._client[settings.DATABASE_NAME]

    async def close(self):
        """Close the MongoDB connection"""
        self._client.close()

    @property
    def database(self) -> AsyncIOMotorDatabase:
        """Access the MongoDB database instance"""
        return self._database


db = AsyncMongoDBSession()
