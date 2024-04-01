# Additional properties to return via API
from pydantic import Field , ConfigDict , field_validator

from app.schemas.response.user_base import UserInDBBase

class User(UserInDBBase):
    hashed_password: bool = Field(default=False, alias="password")
    totp_secret: bool = Field(default=False, alias="totp")
    model_config = ConfigDict(populate_by_name=True)

    @classmethod
    @field_validator("hashed_password", mode="before")
    def evaluate_hashed_password(cls, hashed_password):
        if hashed_password:
            return True
        return False

    @classmethod
    @field_validator("totp_secret", mode="before")
    def evaluate_totp_secret(cls, totp_secret):
        if totp_secret:
            return True
        return False