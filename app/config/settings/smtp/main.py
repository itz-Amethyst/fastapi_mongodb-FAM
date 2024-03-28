from typing import Optional

from pydantic.v1 import BaseSettings


class SMTP(BaseSettings):
    
    SMTP_TLS: bool = True
    SMTP_PORT: Optional[int] = None
    SMTP_HOST: Optional[str] = None
    SMTP_USER: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None