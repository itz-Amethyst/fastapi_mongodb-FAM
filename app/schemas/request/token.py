from typing import Optional
from pydantic import BaseModel, ConfigDict, SecretStr
from odmantic import Model

class RefreshTokenBase(BaseModel):
    token: SecretStr
    authenticates: Optional[Model] = None


class RefreshTokenCreate(RefreshTokenBase):
    authenticates: Model


class RefreshTokenUpdate(RefreshTokenBase):
    pass


class RefreshToken(RefreshTokenUpdate):
    model_config = ConfigDict(from_attributes=True)