from app.config.logger.main import logger_system
from fastapi.openapi.docs import get_swagger_ui_html
from starlette.responses import RedirectResponse , HTMLResponse

from app.setup.factory import create_app
from app.config.settings import settings


app = create_app()

@app.get("/", include_in_schema=False)
def docs_redirect():
    return RedirectResponse(f"/docs")

# Override the documentation endpoint to serve a customized version
@app.get(f"/api/{settings.general.API_V1_STR}/docs", include_in_schema=False)
async def get_docs_v1() -> HTMLResponse:
    """A custom route to override the default swagger UI for the v1 API."""
    return get_swagger_ui_html(
        openapi_url=f"/api/{settings.general.API_V1_STR}/openapi.json",
        title=f"{settings.general.PROJECT_NAME} | Documentation",
        swagger_favicon_url=settings.general.DOCS_FAVICON_PATH,
    )


if __name__ == "__main__":
    import uvicorn

    # Todo
    logger_system.warn("Starting uvicorn in reload mode")
    print(settings.general.HOST_PORT)

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        reload=True,
        port=settings.general.HOST_PORT,
    )