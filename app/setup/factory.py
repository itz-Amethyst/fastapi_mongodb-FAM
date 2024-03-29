from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from starlette import status

from app.config.settings.main import Settings
from app.messages.code.main import responses

from app.setup.helper.middleware import setup_cors_middleware
from app.setup.helper.static import serve_static_app
from app.setup.route.main import setup_routers


tags_metadata = [
    {
        "name": "Authentication",
        "description": "Get authentication token",
    },
    {
        "name": "Users",
        "description": "User registration and management",
    },
    {
        "name": "URLs",
        "description": "Shorten and manage URLs",
    },
]


def create_app():
    description = f"{Settings.general.PROJECT_NAME} API"
    app = FastAPI(
        title=Settings.general.PROJECT_NAME,
        debug = Settings.general.DEBUG,
        version = Settings.general.VERSION,
        openapi_url=f"{Settings.general.API_V1_STR}/openapi.json",
        docs_url="/docs/",
        default_response_class = ORJSONResponse,
        openapi_tags = tags_metadata,
        description=description,
        redoc_url=None,
        responses = {
            status.HTTP_422_UNPROCESSABLE_ENTITY: {
                "description": "Validation Error" ,
                "model": APIValidationError ,  # Adds OpenAPI schema for 422 errors
            } ,
            **{
                code: {
                    "description": HTTPStatus(code).phrase ,
                    "model": CommonHTTPError ,
                }
                for code in responses
            } ,
        } ,
    )
    setup_routers(app)
    setup_cors_middleware(app)
    serve_static_app(app)
    return app





