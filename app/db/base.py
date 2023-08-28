import motor.motor_asyncio
from app.core.config import settings

client = motor.motor_asyncio.AsyncIOMotorClient(settings.DATABASE_URL)

database = client[settings.DATABASE_COLLATION]
