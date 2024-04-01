from typing import Optional

from odmantic import ObjectId
from pydantic import ConfigDict , SecretStr

from app.schemas.request.user import UserBase


class UserInDBBase(UserBase):
    id: Optional[ObjectId] = None
    model_config = ConfigDict(from_attributes=True)



# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: Optional[SecretStr] = None
    totp_secret: Optional[SecretStr] = None
    totp_counter: Optional[int] = None