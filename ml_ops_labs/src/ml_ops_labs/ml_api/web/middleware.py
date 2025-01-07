import uuid
from typing import Any
from contextvars import ContextVar

from starlette.requests import Request
from starlette.middleware.base import BaseHTTPMiddleware
from ml_ops_labs.config import config as settings

_request_id_ctx: ContextVar[str | None] = ContextVar(
    settings.request_id_header, default=None
)


class RequestIDMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = request.headers.get(settings.request_id_header)
        if request_id is None:
            request_id = _generate_request_id()

        set_req_id_operation = _set_request_id(request_id)
        response = await call_next(request)
        response.headers[settings.request_id_header] = request_id

        _request_id_ctx.reset(set_req_id_operation)
        return response


def _get_request_id() -> str | None:
    return _request_id_ctx.get(None)


def _set_request_id(request_id: str) -> Any:
    return _request_id_ctx.set(request_id)


def _generate_request_id() -> str:
    return str(uuid.uuid4())
