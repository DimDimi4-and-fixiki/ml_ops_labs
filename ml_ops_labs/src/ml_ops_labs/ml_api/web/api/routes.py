from fastapi.routing import APIRouter

from ml_ops_labs.ml_api.web.api import echo, monitoring, cats_dogs

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
api_router.include_router(cats_dogs.router, prefix="/cats_dogs", tags=["cats_dogs"])
