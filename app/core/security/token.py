from datetime import datetime, timedelta
from typing import Any, Union

from jose import jwt
import uuid

from app.config.settings import settings


def create_access_token(*, subject: Union[str, Any], expires_delta: timedelta = None, force_totp: bool = False) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(seconds=settings.ACCESS_TOKEN_EXPIRE_SECONDS)
    to_encode = {"exp": expire, "sub": str(subject), "totp": force_totp}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.JWT_ALGO)
    return encoded_jwt


def create_refresh_token(*, subject: Union[str, Any], expires_delta: timedelta = None) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(seconds=settings.REFRESH_TOKEN_EXPIRE_SECONDS)
    to_encode = {"exp": expire, "sub": str(subject), "refresh": True}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.JWT_ALGO)
    return encoded_jwt


def create_magic_tokens(*, subject: Union[str, Any], expires_delta: timedelta = None) -> list[str]:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(seconds=settings.ACCESS_TOKEN_EXPIRE_SECONDS)
    fingerprint = str(uuid.uuid4())
    magic_tokens = []
    # First sub is the user.id, to be emailed. Second is the disposable id.
    for sub in [subject, uuid.uuid4()]:
        to_encode = {"exp": expire, "sub": str(sub), "fingerprint": fingerprint}
        encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.JWT_ALGO)
        magic_tokens.append(encoded_jwt)
    return magic_tokens


