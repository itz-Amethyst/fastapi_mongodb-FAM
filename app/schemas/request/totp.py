from typing import Optional
from pydantic import BaseModel, SecretStr

class EnableTOTP(BaseModel):
    claim: str
    uri: str
    password: Optional[SecretStr] = None