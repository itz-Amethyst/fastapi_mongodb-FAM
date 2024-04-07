from __future__ import annotations
from motor.core import AgnosticDatabase

from app.crud.base import CRUDBase
from app.models import User, Token
from app.schemas import RefreshTokenCreate, RefreshTokenUpdate
from app.schemas.response.pagination import PaginationParams
from app.schemas.response.sorting import SortingParams


class CRUDToken(CRUDBase[Token, RefreshTokenCreate, RefreshTokenUpdate]):
    # Everything is user-dependent

    def __init__(self):
        super().__init__()
        self.offset_token = None
        self.user = None
        self._is_child_crud_token = True

    async def create(self, db: AgnosticDatabase, *, obj_in: str, user_obj: User) -> Token:
        db_obj = await self.engine.find_one(self.model, self.model.token == obj_in)
        if db_obj:
            if db_obj.authenticates_id != user_obj.id:
                raise ValueError("Token mismatch between key and user.")
            return db_obj
        else:
            new_token = self.model(token=obj_in, authenticates_id=user_obj)
            user_obj.refresh_tokens.append(new_token.id)
            await self.engine.save_all([new_token, user_obj])
            return new_token

    async def get(self, *, user: User, token: str) -> Token:
        return await self.engine.find_one(User, ((User.id == user.id) & (User.refresh_tokens == token)))


    async def get_multi(self, *, user: User, page_break: bool = False, paging_params: "PaginationParams",
        sorting_params: "SortingParams") -> list[Token]:
        # Todo
        offset = {"skip": paging_params.skip , "limit": paging_params.limit} if page_break else {}

        self.user = user
        self.offset_token = offset
        return await super().get_multi(db=None, page_break=page_break, paging_params=paging_params,
                                        sorting_params=sorting_params)

    async def remove(self, db: AgnosticDatabase, *, db_obj: Token) -> None:
        users = []
        async for user in self.engine.find(User, User.refresh_tokens.in_([db_obj.id])):
            user.refresh_tokens.remove(db_obj.id)
            users.append(user)
        await self.engine.save(users)
        await self.engine.delete(db_obj)


token = CRUDToken(Token)