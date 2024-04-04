import secrets

from pydantic_settings import BaseSettings, SettingsConfigDict

from app.config.settings.helper import DOTENV , config


class TOTP(BaseSettings):
    TOTP_ALGO: str = config.get("TOTP_ALGO" , "SHA-1")
    TOTP_SECRET_KEY: str = config.get("TOTP_SECRET_KEY" , secrets.token_urlsafe(32))

    model_config = SettingsConfigDict(env_file = '../../../../.env' , extra = 'allow')
