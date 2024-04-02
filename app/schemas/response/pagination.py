from typing import Generic, List, TypeVar
from odmantic import Model
from pydantic import Field , BaseModel
from pydantic.generics import GenericModel

SchemaType = TypeVar("SchemaType", bound= Model)


class Paginated(GenericModel, Generic[SchemaType]):
    page: int
    limit: int
    total: int
    results: List[SchemaType]


class PaginationParams(BaseModel):
    page: int = Field(1, ge=1)
    MULTI_MAX: int = Field(12, ge = 2, le = 20)

    @property
    def skip(self) -> int:
        return (self.page - 1) * self.per_page

    @property
    def limit(self) -> int:
        return self.MULTI_MAX