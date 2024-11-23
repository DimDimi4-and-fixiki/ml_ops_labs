from ml_ops_labs.config import config


def get_dsn(with_params: bool = False) -> str:
    url = f"postgresql://{config.db_user}:{config.db_pass}@{config.db_host}:{config.db_port}/{config.db_name}"

    if with_params:
        url += "?maxsize=10" + "&minsize=4"

    return url
