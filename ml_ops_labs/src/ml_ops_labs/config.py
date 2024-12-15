import enum
from pydantic_settings import BaseSettings


class LogLevel(str, enum.Enum):
    """Possible log levels."""

    NOTSET = "NOTSET"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FATAL = "FATAL"


class Settings(BaseSettings):
    """
    Application settings.

    These parameters can be configured
    with environment variables.
    """

    host: str = "127.0.0.1"
    port: int = 8080
    # quantity of workers for uvicorn
    workers_count: int = 1
    # Enable uvicorn reloading
    reload: bool = False
    # Current environment
    environment: str = "dev"
    log_level: LogLevel = LogLevel.INFO
    request_id_header: str = "x-request-id"

    db_user: str = "ml_ops"
    db_pass: str = "ml_ops"
    db_name: str = "ml_ops_db"
    db_host: str = "0.0.0.0"
    db_port: str = "5433"
    db_connection_attempts: int = 4


config = Settings()
