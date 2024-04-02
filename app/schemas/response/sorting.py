from enum import Enum
from pydantic import BaseModel


class SortOrder(Enum):
    ASC = "asc"
    DESC = "desc"


class SortingParams(BaseModel):
    sort: str = "created_at"
    order: SortOrder = SortOrder.ASC