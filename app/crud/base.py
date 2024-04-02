from typing import Any, Dict, Generic, Optional, Type, TypeVar, Union

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from motor.core import AgnosticDatabase
from odmantic import AIOEngine

from app.db.base import BaseModel_DB
from app.config.settings.main import Settings
from app.db.session import get_engine
from app.schemas.response.pagination import Paginated , PaginationParams
from app.schemas.response.sorting import SortOrder , SortingParams

ModelType = TypeVar("ModelType", bound=BaseModel_DB)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model
        self.engine: AIOEngine = get_engine()

    async def get(self, db: AgnosticDatabase, id: Any) -> Optional[ModelType]:
        return await self.engine.find_one(self.model, self.model.id == id)


    async def get_multi(self, db: AgnosticDatabase, *, page_break: bool = False, paging_params: "PaginationParams",
        sorting_params: "SortingParams",) -> list[ModelType]:

        offset = {"skip": paging_params.skip, "limit": paging_params.limit} if page_break else {}
        # Sorting
        sort_field = getattr(self.model , sorting_params.sort) if hasattr(self.model , sorting_params.sort) else getattr(self.model , sorting_params.sort , "created_at")
        if sort_field is None:
            raise ValueError(f"Invalid sort field: {sorting_params.sort}")
        sort_expr = sort_field.desc() if sorting_params.order == SortOrder.DESC else sort_field.asc()
        result = self.engine.find(self.model, sort = sort_expr, **offset)
        return await Paginated(
            page = paging_params.page,
            limit = paging_params.limit,
            total = self.engine.count(self.model),
            results = result
        )


    async def create(self, db: AgnosticDatabase, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)
        return await self.engine.save(db_obj)

    async def update(
        self, db: AgnosticDatabase, *, db_obj: ModelType, obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        obj_data = jsonable_encoder(db_obj)
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)
        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        # TODO: Check if this saves changes with the setattr calls
        await self.engine.save(db_obj)
        return db_obj

    async def remove(self, db: AgnosticDatabase, *, id: int) -> ModelType:
        obj = await self.model.get(id)
        if obj:
            await self.engine.delete(obj)
        return obj