from app.models import Account
from app.schemas.response.main import ResponseWithPagination
from app.manager.account import AccountManager
from app.routes.base import router
router.tags = ['User']


@router.get("/users", response_model=ResponseWithPagination[Account])
async def get_users(
    page: int = 1,
    limit: int = 10,
    columns: str = None,
    sort: str = None,
    filter: str = None
):
    query = await AccountManager.get_all(page=page, limit=limit, columns=columns, sort=sort, filter=filter)
    # return await ResponseWithPagination.simulate(query, page, limit, db)