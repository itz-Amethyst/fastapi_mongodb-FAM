from fastapi import FastAPI

from app.setup.helpers.route_name import use_route_names_as_operation_ids


def setup_routers(app: FastAPI) -> None:
    app.include_router()

    # app.include_router(
    #     fastapi_users.get_users_router(
    #         UserRead, UserUpdate, requires_verification=False
    #     ),
    #     prefix=f"{settings.API_PATH}/users",
    #     tags=["users"],
    # )
    # The following operation needs to be at the end of this function
    use_route_names_as_operation_ids(app)