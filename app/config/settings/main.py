from functools import lru_cache

from pydantic import PostgresDsn
from pydantic.v1 import BaseSettings
from pydantic_core import MultiHostUrl


class Settings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    PGADMIN_EMAIL: str
    PGADMIN_PASSWORD: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    DATE_FORMAT: str

    @computed_field  # type: ignore[misc]
    @property
    def SQLALCHEMY_DATABASE_URI( self ) -> PostgresDsn:
        return MultiHostUrl.build(
            scheme = "postgresql+psycopg" ,
            username = self.POSTGRES_USER ,
            password = self.POSTGRES_PASSWORD ,
            host = self.POSTGRES_SERVER ,
            port = self.POSTGRES_PORT ,
            path = self.POSTGRES_DB ,
        )

    class Config:
        env_file = "./.env"


@lru_cache(maxsize = 1)
def get_settings():
    return Settings()


settings = get_settings()