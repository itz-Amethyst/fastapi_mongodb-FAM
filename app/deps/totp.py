from fastapi import Depends, HTTPException, status
from motor.core import AgnosticDatabase

from app import crud, models
from app.deps import reusable_oauth2
from app.deps.token import get_token_payload
from app.deps.db import get_db

async def get_totp_user(db: AgnosticDatabase = Depends(get_db), token: str = Depends(reusable_oauth2)) -> models.User:
    token_data = get_token_payload(token)
    if token_data.refresh or not token_data.totp:
        # Refresh token is not a valid access token and TOTP False cannot be used to validate TOTP
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = await crud.user.get(db, id=token_data.sub)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user