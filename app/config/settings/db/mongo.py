from pydantic_settings import BaseSettings

from app.config.settings.helper import config


class MongoDB(BaseSettings):
    
    MONGO_DATABASE: str = config.get("MONGO_DATABASE")
    MONGO_DATABASE_URI: str = config.get("MONGO_DATABASE_URI")
