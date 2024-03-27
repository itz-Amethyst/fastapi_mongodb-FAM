import uuid

from sqlalchemy import Uuid , String
from sqlalchemy.orm import Mapped , mapped_column , relationship

from app.models.base import Base


class User(Base):
    __tablename__ = 'user_account'

    user_id: Mapped[str] = mapped_column(
        Uuid(as_uuid = False) , primary_key = True , default = lambda _: str(uuid.uuid4())
    )
    email: Mapped[str] = mapped_column(
        String(256) , nullable = False , unique = True , index = True
    )
    hashed_password: Mapped[str] = mapped_column(String(128) , nullable = False)
    refresh_tokens: Mapped[list["RefreshToken"]] = relationship(back_populates = "user")