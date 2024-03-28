from typing import Optional

from pydantic import EmailStr , field_validator
from pydantic.v1 import BaseSettings
from pydantic_core.core_schema import ValidationInfo


class Email(BaseSettings):
    EMAILS_FROM_EMAIL: Optional[EmailStr] = None
    EMAILS_FROM_NAME: Optional[str] = None
    EMAILS_TO_EMAIL: Optional[EmailStr] = None

    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48
    EMAIL_TEMPLATES_DIR: str = "/app/app/email-templates/build"
    EMAILS_ENABLED: bool = False

    @classmethod
    @field_validator("EMAILS_ENABLED" , mode = "before")
    def get_emails_enabled( cls , v: bool , info: ValidationInfo ) -> bool:
        return bool(info.data.get("SMTP_HOST") and info.data.get("SMTP_PORT") and info.data.get("EMAILS_FROM_EMAIL"))

    @classmethod
    @field_validator("EMAILS_FROM_NAME")
    def get_project_name( cls , v: Optional[str] , info: ValidationInfo ) -> str:
        if not v:
            return info.data["PROJECT_NAME"]
        return v

    EMAIL_TEST_USER: EmailStr = "test@example.com"