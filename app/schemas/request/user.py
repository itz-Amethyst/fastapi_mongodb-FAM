from typing import Optional
from typing_extensions import Annotated
from pydantic import BaseModel, EmailStr, StringConstraints


class UserLogin(BaseModel):
    username: str
    password: str


# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    email_validated: Optional[bool] = False
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    full_name: str = ""


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: Optional[Annotated[str, StringConstraints(min_length=8, max_length=64)]] = None


# Properties to receive via API on update
class UserUpdate(UserBase):
    original: Optional[Annotated[str, StringConstraints(min_length=8, max_length=64)]] = None
    password: Optional[Annotated[str, StringConstraints(min_length=8, max_length=64)]] = None


