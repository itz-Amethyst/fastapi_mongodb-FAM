from app.config.settings import settings
from fastapi.security import OAuth2PasswordBearer

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl=f"api/{settings.general.API_V1_STR}/login/oauth")
