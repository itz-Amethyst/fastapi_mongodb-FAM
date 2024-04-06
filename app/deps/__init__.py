from fastapi.security import OAuth2PasswordBearer

from app.config.settings import settings

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl=f"api/{settings.API_V1_STR}/login/oauth")