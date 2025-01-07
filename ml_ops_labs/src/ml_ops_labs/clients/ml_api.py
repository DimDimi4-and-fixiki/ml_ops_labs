import requests

from ml_ops_labs.ml_api.web.api.cats_dogs.model import MlModelT, PetT
from ml_ops_labs.config import config
from pathlib import Path
from loguru import logger

URL = f"{config.ml_api_url}/api/cats_dogs"


def predict_pet(model_type: MlModelT, file_path: Path) -> PetT:
    url = f"{URL}/detect_pet?model_type={model_type}"
    logger.info(f"URL = {url}")
    files = {
        "image": (str(file_path), open(file_path, "rb"), "image/jpeg"),
    }

    response = requests.post(url=url, files=files)
    logger.info(response.text)
    resp = response.json()

    return resp["predict"]
