import uvicorn

from ml_ops_labs.config import config as settings


def main() -> None:
    """Entrypoint of the application."""

    uvicorn.run(
        "ml_ops_labs.ml_api.web.application:get_app",
        workers=settings.workers_count,
        host=settings.host,
        port=settings.port,
        reload=settings.reload,
        log_level=settings.log_level.value.lower(),
        factory=True,
    )


if __name__ == "__main__":
    main()
