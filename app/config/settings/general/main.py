import secrets
from typing import List , Optional , Union

from pydantic import AnyHttpUrl , field_validator , HttpUrl , EmailStr , validator
from pydantic.v1 import BaseSettings


class General(BaseSettings):
    SECRET_KEY: str = secrets.token_urlsafe(32)

    API_V1_STR: str = "/api/v1"

    SERVER_NAME: str
    SERVER_HOST: AnyHttpUrl
    SERVER_BOT: str = "Symona"

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    PROJECT_NAME: str
    SENTRY_DSN: Optional[HttpUrl] = None

    # GENERAL SETTINGS
    MULTI_MAX: int = 20

    FIRST_SUPERUSER: EmailStr
    FIRST_SUPERUSER_PASSWORD: str
    USERS_OPEN_REGISTRATION: bool = True

    @classmethod
    @validator("BACKEND_CORS_ORIGINS" , pre = True)
    def assemble_cors_origins( self , v: Union[str , List[str]] ) -> Union[List[str] , str]:
        if isinstance(v , str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v , (list , str)):
            return v
        raise ValueError(v)

    #
    @classmethod
    @validator("SENTRY_DSN" , pre = True)
    def sentry_dsn_can_be_blank( self , v: str ) -> Optional[str]:
        if isinstance(v , str) and len(v) == 0:
            return None
        return v