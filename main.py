from fastapi.logger import logger
from starlette.responses import RedirectResponse

from app.setup.factory import create_app


app = create_app()

@app.get("/", include_in_schema=False)
def docs_redirect():
    return RedirectResponse(f"/docs")



if __name__ == "__main__":
    import uvicorn

    logger.info("Starting uvicorn in reload mode")
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        reload=True,
        port=int("{{ cookiecutter.backend_port }}"),
    )