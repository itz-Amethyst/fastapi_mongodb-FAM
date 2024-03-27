import math
from typing import TypeVar , Optional , Generic , List

from pydantic import BaseModel
from pydantic.v1.generics import GenericModel
from sqlalchemy import Select , select , func
from sqlalchemy.ext.asyncio import AsyncSession

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

    @classmethod
    async def simulate( cls , query: Select , page: int , limit: int , db: AsyncSession ):
        total_record = await db.execute(select(func.count(1)).select_from(query)).scalar() or 0
        total_pages = math.ceil(total_record / limit)
        offset_page = page - 1
        result = await db.execute(query.offset(offset_page * limit).limit(limit))
        content = result.fetchall()
        return cls(
            page_number = page ,
            page_size = limit ,
            total_pages = total_pages ,
            total_record = total_record ,
            content = content
        )