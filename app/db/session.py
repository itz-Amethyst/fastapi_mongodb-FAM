from app.config.settings.main import Settings
from odmantic import AIOEngine
from motor.core import AgnosticDatabase
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.driver_info import DriverInfo

Driver_Info = DriverInfo(name = 'FAM', version = '0.2.0')

class _MongoClientSingleton:
    _instance = None

    def __new__( cls ):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._initialize_mongodb_client()
        return cls._instance

    def _initialize_mongodb_client( self ):
        self.mongodb_client = AsyncIOMotorClient(Settings.database.MONGO_DATABASE_URI , driver = Driver_Info)
        self.engine = AIOEngine(client = self.mongodb_client , database = Settings.database.MONGO_DATABASE)

def MongoDataBase() -> AgnosticDatabase:
    return _MongoClientSingleton().mongodb_client[Settings.database.MONGO_DATABASE]

def get_engine() -> AIOEngine:
    return _MongoClientSingleton().engine

async def ping():
    await MongoDataBase().command('ping')

__all__ = ["MongoDataBase", "ping"]