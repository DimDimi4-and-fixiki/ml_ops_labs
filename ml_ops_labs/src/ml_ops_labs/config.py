from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application settings.

    These parameters can be configured
    with environment variables.
    """

    db_user: str = "ml_ops"
    db_pass: str = "ml_ops"
    db_name: str = "ml_ops_db"
    db_host: str = "0.0.0.0"
    db_port: str = "5433"
    db_connection_attempts: int = 4


config = Settings()
