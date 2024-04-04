from pydantic_settings import BaseSettings, SettingsConfigDict

from app.config.settings.helper import DOTENV , config


class JWT(BaseSettings):
    # 60 minutes * 24 hours * 8 days = 8 days

    ACCESS_TOKEN_EXPIRE_SECONDS: int = config.get("ACCESS_TOKEN_EXPIRE_SECONDS" , 60 * 30)
    REFRESH_TOKEN_EXPIRE_SECONDS: int = config.get("REFRESH_TOKEN_EXPIRE_SECONDS" , 60 * 60 * 24 * 30)
    JWT_ALGO: str = config.get("JWT_ALGO" , "HS512")

    # model_config = SettingsConfigDict(env_file = '../../../../.env' , extra = 'allow')