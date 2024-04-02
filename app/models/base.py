from datetime import datetime

from odmantic import Field

from app.db.base import BaseModel_DB

def datetime_now_sec():
    return datetime.now().replace(microsecond=0)

def table_name_decorator(cls):
    # Get the table name from the class name (convert to lowercase)
    cls.Settings.name = cls.__name__.lower()
    return cls

@table_name_decorator
class Base(BaseModel_DB):
    create_time: datetime = Field(default_factory = datetime_now_sec)
    modified: datetime = Field(default_factory = datetime_now_sec, )

    class Settings:
        use_state_management = True