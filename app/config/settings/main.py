from functools import lru_cache

from pydantic import PostgresDsn
from pydantic.v1 import BaseSettings
from pydantic_core import MultiHostUrl
from app.config.settings.db.main import Database


class Settings(BaseSettings):

    database: Database
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    DATE_FORMAT: str

    @computed_field  # type: ignore[misc]
    @property
    def SQLALCHEMY_DATABASE_URI( self ) -> PostgresDsn:
        return MultiHostUrl.build(
            scheme = "postgresql+psycopg" ,
            username = self.database.POSTGRES_USER ,
            password = self.database.POSTGRES_PASSWORD ,
            host = self.database.POSTGRES_SERVER ,
            port = self.database.POSTGRES_PORT ,
            path = self.database.POSTGRES_DB ,
        )

    class Config:
        env_file = "./.env"


@lru_cache(maxsize = 1)
def get_settings():
    return Settings()


settings = get_settings()