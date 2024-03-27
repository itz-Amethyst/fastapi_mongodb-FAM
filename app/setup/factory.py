from fastapi import FastAPI

from app.core.config import settings

from app.setup.helper.middleware import setup_cors_middleware
from app.setup.helper.static import serve_static_app
from app.setup.route.main import setup_routers


def create_app():
    description = f"{settings.PROJECT_NAME} API"
    app = FastAPI(
        title=settings.PROJECT_NAME,
        openapi_url=f"{settings.API_PATH}/openapi.json",
        docs_url="/docs/",
        description=description,
        redoc_url=None,
    )
    setup_routers(app)
    setup_cors_middleware(app)
    serve_static_app(app)
    return app





