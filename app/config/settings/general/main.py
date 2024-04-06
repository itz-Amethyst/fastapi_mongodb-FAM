import os
import secrets
from pathlib import Path
from typing import List , Optional , Union

from pydantic import AnyHttpUrl , field_validator , HttpUrl , EmailStr, ConfigDict
from app import __version__
from app.config.settings.helper import DOTENV
from dotenv import load_dotenv, dotenv_values
from app.core.enums.log import LogLevel
from pydantic_settings import BaseSettings, SettingsConfigDict
from app.config.settings.helper import config

class General(BaseSettings):
    SECRET_KEY: str = secrets.token_urlsafe(32)
    DEBUG: bool = config.get("DEBUG" , True)
    VERSION: str = config.get("VERSION" , __version__)
    LOG_LEVEL: str = config.get("LOG_LEVEL" , "INFO")
    ENABLE_FILE_LOG_SYSTEM: bool = config.get("ENABLE_FILE_LOG_SYSTEM" , True)
    DOCS_FAVICON_PATH: Path = config.get("DOCS_FAVICON_PATH" , "test/fav.ico")
    HOST_PORT: int = config.get("HOST_PORT" , 8000)

    API_V1_STR: str = config.get("API_V1_STR" , "v1")

    SERVER_NAME: str = config.get("SERVER_NAME" , "Test_name")
    SERVER_HOST: AnyHttpUrl = config.get("SERVER_HOST" , "http://localhost")
    SERVER_BOT: str = config.get("SERVER_BOT" , "Symona")

    BACKEND_CORS_ORIGINS: Union[List[AnyHttpUrl], str] = config.get("BACKEND_CORS_ORIGINS" , [])

    PROJECT_NAME: str = config.get("PROJECT_NAME" , "")
    SENTRY_DSN: Optional[HttpUrl] = config.get("SENTRY_DSN" , None)

    # GENERAL SETTINGS
    MULTI_MAX: int = config.get("MULTI_MAX" , 12)

    FIRST_SUPERUSER: EmailStr = config.get("FIRST_SUPERUSER" , "")
    FIRST_SUPERUSER_PASSWORD: str = config.get("FIRST_SUPERUSER_PASSWORD" , "")
    USERS_OPEN_REGISTRATION: bool = config.get("USERS_OPEN_REGISTRATION" , True)

    @classmethod
    @field_validator("BACKEND_CORS_ORIGINS" , mode = "before")
    def assemble_cors_origins( cls , v: Union[str , List[str]] ) -> Union[List[str] , str]:
        if isinstance(v , str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v , (list , str)):
            return v
        raise ValueError(v)

    @classmethod
    @field_validator("SENTRY_DSN" , mode = "before")
    def sentry_dsn_can_be_blank( cls , v: str ) -> Optional[str]:
        if isinstance(v , str) and len(v) == 0:
            return None
        return v

    # model_config = SettingsConfigDict(env_file = DOTENV , extra = 'allow' , case_sensitive = False)