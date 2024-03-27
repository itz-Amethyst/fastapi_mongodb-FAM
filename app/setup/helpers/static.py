from starlette.requests import Request
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles


def serve_static_app(app):
    app.mount("/", StaticFiles(directory="static"), name="static")

    @app.middleware("http")
    async def _add_404_middleware(request: Request, call_next):
        """Serves static assets on 404"""
        response = await call_next(request)
        path = request["path"]
        if path.startswith(settings.API_PATH) or path.startswith("/docs"):
            return response
        if response.status_code == 404:
            return FileResponse("static/index.html")
        return response


