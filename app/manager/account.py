import math

from sqlalchemy import update, delete, or_, text, func, column
from sqlalchemy.sql import select

# from app.config import db, commit_rollback
from app.manager.helper.converts import convert_sort , convert_columns
from app.models import Account
# from app.schema import PersonCreate, PageResponse

class AccountManager:

    @staticmethod
    async def get_all(
            page: int = 1 ,
            limit: int = 10 ,
            columns: str = None ,
            sort: str = None ,
            filter: str = None
    ):
        query = select(from_obj = Account , columns = "*")

        # select columns dynamically
        if columns is not None and columns != "all":
            query = select(from_obj = Account , columns = convert_columns(columns))

        # select filter dynamically
        if filter is not None and filter != "null":
            criteria = dict(x.split("*") for x in filter.split('-'))
            criteria_list = []
            for attr , value in criteria.items():
                _attr = getattr(Account , attr)
                search = f"%{value}%"
                criteria_list.append(_attr.like(search))
            query = query.filter(or_(*criteria_list))

        # select sort dynamically
        if sort is not None and sort != "null":
            query = query.order_by(text(convert_sort(sort)))

        return query