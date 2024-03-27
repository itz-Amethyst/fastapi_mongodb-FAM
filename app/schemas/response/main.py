from typing import TypeVar , Optional , Generic , List

from pydantic import BaseModel
from pydantic.v1.generics import GenericModel

T = TypeVar('T')


class ResponseSchema(BaseModel):
    message: str
    result: Optional[T] = None

class ResponseWithPagination(GenericModel, Generic[T]):
    """ The response for a pagination query. """

    page_number: int
    page_size: int
    total_pages: int
    total_record: int
    content: List[T]