from pydantic.v1 import BaseSettings


class JWT(BaseSettings):
    # 60 minutes * 24 hours * 8 days = 8 days

    ACCESS_TOKEN_EXPIRE_SECONDS: int = 60 * 30
    REFRESH_TOKEN_EXPIRE_SECONDS: int = 60 * 60 * 24 * 30
    JWT_ALGO: str = "HS512"