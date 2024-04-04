from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict

from app.config.settings.helper import DOTENV , config


class SMTP(BaseSettings):
    SMTP_TLS: bool = config.get("SMTP_TLS" , True)
    SMTP_PORT: Optional[int] = config.get("SMTP_PORT" , None)
    SMTP_HOST: Optional[str] = config.get("SMTP_HOST" , None)
    SMTP_USER: Optional[str] = config.get("SMTP_USER" , None)
    SMTP_PASSWORD: Optional[str] = config.get("SMTP_PASSWORD" , None)

    # model_config = SettingsConfigDict(env_file = '../../../../.env' , extra = 'allow')