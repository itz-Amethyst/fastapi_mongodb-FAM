from typing import Optional
from pydantic import BaseModel, SecretStr
from odmantic import ObjectId



class Token(BaseModel):
    access_token: SecretStr
    refresh_token: Optional[SecretStr] = None
    token_type: str


class TokenPayload(BaseModel):
    sub: Optional[ObjectId] = None
    refresh: Optional[bool] = False
    totp: Optional[bool] = False


class MagicTokenPayload(BaseModel):
    sub: Optional[ObjectId] = None
    fingerprint: Optional[ObjectId] = None


class WebToken(BaseModel):
    claim: str