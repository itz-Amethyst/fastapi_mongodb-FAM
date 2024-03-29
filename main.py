from fastapi.logger import logger
from fastapi.openapi.docs import get_swagger_ui_html
from starlette.responses import RedirectResponse , HTMLResponse

from app.config.settings.main import Settings
from app.setup.factory import create_app


app = create_app()

@app.get("/", include_in_schema=False)
def docs_redirect():
    return RedirectResponse(f"/docs")

# Override the documentation endpoint to serve a customized version
@app.get(f"/api/{Settings.general.API_V1_STR}/docs", include_in_schema=False)
async def get_docs_v1() -> HTMLResponse:
    """A custom route to override the default swagger UI for the v1 API."""
    return get_swagger_ui_html(
        openapi_url=f"/api/{Settings.general.API_V1_STR}/openapi.json",
        title=f"{Settings.general.PROJECT_NAME} | Documentation",
        swagger_favicon_url=Settings.general.DOCS_FAVICON_PATH,
    )


if __name__ == "__main__":
    import uvicorn

    logger.info("Starting uvicorn in reload mode")
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        reload=True,
        port=Settings.general.HOST_PORT,
    )