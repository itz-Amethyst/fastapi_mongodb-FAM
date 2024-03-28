from pydantic.v1 import BaseSettings


class MongoDB(BaseSettings):
    
    MONGO_DATABASE: str
    MONGO_DATABASE_URI: str