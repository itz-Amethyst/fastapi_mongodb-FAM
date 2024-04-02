from __future__ import annotations

from datetime import datetime

from odmantic import Reference , Field

from app.models.base import Base

from app.models.user.main import User


class Token(Base):
    token: str
    authenticates_id: User = Reference()
    used: bool = Field(default = False)
    expiration_date: datetime