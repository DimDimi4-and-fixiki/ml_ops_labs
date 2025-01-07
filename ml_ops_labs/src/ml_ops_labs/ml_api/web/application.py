from fastapi import FastAPI
from fastapi.responses import UJSONResponse

from ml_ops_labs.ml_api.web.api.routes import api_router
from ml_ops_labs.ml_api.web.lifetime import (
    register_shutdown_event,
    register_startup_event,
)
from ml_ops_labs.ml_api.web.middleware import RequestIDMiddleware


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """
    app = FastAPI(
        title="ml_api",
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        openapi_url="/api/openapi.json",
        default_response_class=UJSONResponse,
    )

    # Adds startup and shutdown events.
    register_startup_event(app)
    register_shutdown_event(app)

    # Main router for the API.
    app.include_router(router=api_router, prefix="/api")

    # Middlewares
    app.add_middleware(RequestIDMiddleware)
    return app
