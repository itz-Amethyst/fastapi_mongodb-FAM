from typing import Optional , Union

from app.config.settings import settings
from passlib.exc import TokenError, MalformedTokenError
from app.schemas.response.totp import NewTOTP

from passlib.totp import TOTP

totp_factory: TOTP = TOTP.using(secrets={"1": settings.TOTP_SECRET_KEY}, issuer=settings.SERVER_NAME, alg=settings.TOTP_ALGO)


def create_new_totp(*, label: str, uri: Optional[str] = None) -> NewTOTP:
    if not uri:
        totp = totp_factory.new()
    else:
        totp = totp_factory.from_source(uri)
    return NewTOTP(
        **{
            "secret": totp.to_json(),
            "key": totp.pretty_key(),
            "uri": totp.to_uri(issuer=settings.general.SERVER_NAME, label=label),
        }
    )


def verify_totp(*, token: str, secret: str, last_counter: int = None) -> Union[str, bool]:
    """
    token: from user
    secret: totp security string from user in db
    last_counter: int from user in db (can be None)
    """
    try:
        match = totp_factory.verify(token, secret, last_counter=last_counter)
    except (MalformedTokenError, TokenError):
        return False
    else:
        return match.counter


