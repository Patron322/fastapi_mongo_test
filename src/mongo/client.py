from motor.motor_asyncio import AsyncIOMotorClient

from settings.settings import SETTINGS

client = AsyncIOMotorClient(f"mongodb://{SETTINGS.MONGO_HOST}:{SETTINGS.MONGO_PORT}")["local"]["collections"]
