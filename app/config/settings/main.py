from functools import lru_cache
from pydantic_settings import BaseSettings

from app.config.settings.db.mongo import MongoDB
from app.config.settings.email.main import Email
from app.config.settings.general.main import General
from app.config.settings.jwt.main import JWT
from app.config.settings.smtp.main import SMTP
from app.config.settings.totp.main import TOTP

#! This adds support for 'mongodb+srv' connection schemas when using e.g. MongoDB Atlas
# https://www.mongodb.com/developer/products/mongodb/srv-connection-strings/
# MongoDsn.allowed_schemes.add("mongodb+srv")


class Settings(BaseSettings):

    # For Postgresql
    # database: Database

    database: MongoDB = MongoDB()
    # test_value: str
    email_platform: Email = Email()
    general: General = General()
    jwt: JWT = JWT()
    smtp: SMTP = SMTP()
    # service: Service
    totp: TOTP = TOTP()


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



@lru_cache(maxsize = 1)
def get_settings() -> Settings:
    return Settings()

