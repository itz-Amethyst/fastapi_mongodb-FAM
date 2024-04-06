from app.utils.logger import logger_system
from starlette.responses import RedirectResponse

from app.setup.factory import create_app
from app.config.settings import settings


app = create_app()

@app.get("/", include_in_schema=False)
def docs_redirect():
    return RedirectResponse(f"/api/{settings.general.API_V1_STR}/docs")


logger_system.info("Starting uvicorn in reload mode")

if __name__ == "__main__":
    import uvicorn


    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        reload=True,
        port=settings.general.HOST_PORT,
    )

    # Todo
    print(settings.general.HOST_PORT)