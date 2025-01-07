from ml_ops_labs.ml_models.cats_dogs import load_cnn_1_model
from ml_ops_labs.ml_api.web.api.cats_dogs.model import PetT
from loguru import logger
from keras.api.preprocessing.image import load_img
import numpy as np
import pathlib

model_1 = load_cnn_1_model()


def get_predict_cnn(img_path: pathlib.Path) -> PetT:
    logger.info(f"Loading {img_path} for predict")
    img = load_img(img_path, target_size=(224, 224))
    img_array = np.array(img).reshape(1, 224, 224, 3)
    a = model_1.predict(img_array)
    if a == [[0]]:
        return "cat"
    return "dog"


def get_predict_linear(img_path: pathlib.Path) -> PetT:
    logger.info(f"Loading {img_path} for predict")
    hash = get_hash(img_path)
    predict = int(hash) * 1 / 5 + 15
    if predict % 2 == 0:
        return "cat"
    return "dog"


def get_hash(img_path) -> int:
    img = load_img(img_path, target_size=(224, 224))
    img_array = np.array(img)
    img_sum = int(np.sum(img_array.sum(axis=1)))
    logger.info(f"hash = {img_sum}")
    return img_sum
