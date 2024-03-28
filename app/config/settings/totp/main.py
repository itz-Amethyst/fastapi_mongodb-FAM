import secrets

from pydantic.v1 import BaseSettings


class TOTP(BaseSettings):
    TOTP_ALGO: str = "SHA-1"
    TOTP_SECRET_KEY: str = secrets.token_urlsafe(32)
