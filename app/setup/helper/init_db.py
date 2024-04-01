from pymongo.database import Database

from app import crud
from app.config.settings.main import Settings

FIRST_SUPERUSER = Settings.general.FIRST_SUPERUSER

async def init_db(db: Database) -> None:
    user = await crud.user.get_by_email(db, email=FIRST_SUPERUSER)
    if not user:
        # Create user auth
        user_in = schemas.UserCreate(
            email=FIRST_SUPERUSER,
            password=Settings.general.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
            full_name=FIRST_SUPERUSER,
        )
        user = await crud.user.create(db, obj_in=user_in)  # noqa: F841