from functools import lru_cache
from pathlib import Path

from pydantic.v1 import BaseSettings
from pydantic import MongoDsn
from app.config.settings import MongoDB, Email, General, JWT, SMTP, Service, TOTP

#! This adds support for 'mongodb+srv' connection schemas when using e.g. MongoDB Atlas
# https://www.mongodb.com/developer/products/mongodb/srv-connection-strings/
# MongoDsn.allowed_schemes.add("mongodb+srv")

PROJECT_DIR: Path = Path(__file__).parent.parent.parent


class Settings(BaseSettings):

    # For Postgresql
    # database: Database

    database: MongoDB
    email_platform: Email
    general: General
    jwt: JWT
    smtp: SMTP
    service: Service
    totp: TOTP


    # @computed_field
    # @property
    # def SQLALCHEMY_DATABASE_URI( self ) -> PostgresDsn:
    #     return MultiHostUrl.build(
    #         scheme = "postgresql+psycopg" ,
    #         username = self.database.POSTGRES_USER ,
    #         password = self.database.POSTGRES_PASSWORD.get_secret_value() ,
    #         host = self.database.POSTGRES_SERVER ,
    #         port = self.database.POSTGRES_PORT ,
    #         path = self.database.POSTGRES_DB ,
    #     )

    class Config:
        env_file = f"{PROJECT_DIR}/.env"
        case_sensitive=False


@lru_cache(maxsize = 1)
def get_settings() -> Settings:
    return Settings()

