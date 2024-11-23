import keras
from ml_ops_labs.ml_models.models import MODELS_DIR
from keras.api.models import load_model


def load_cats_model() -> keras.Sequential:
    model_path = MODELS_DIR / "catvsdog.h5"
    model = load_model(model_path)
    return model
