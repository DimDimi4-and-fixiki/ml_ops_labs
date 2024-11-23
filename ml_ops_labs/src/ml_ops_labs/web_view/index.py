import streamlit as st
from ml_ops_labs.ml_models.cats_dogs import load_cats_model
from loguru import logger
from keras.api.preprocessing.image import load_img
from streamlit.runtime.uploaded_file_manager import UploadedFile
import numpy as np
import tempfile
from PIL.Image import Image
import pathlib


model = load_cats_model()


def get_predict(img_path: pathlib.Path) -> (str, Image):
    logger.info(f"Loading {img_path} for predict")
    img = load_img(img_path, target_size=(224, 224))
    img_array = np.array(img).reshape(1, 224, 224, 3)
    a = model.predict(img_array)
    if a == [[0]]:
        return "cat", img
    return "dog", img


def index() -> None:
    st.title("Cats VS Dogs classifier")
    upload_file = st.file_uploader(label="Upload image", type=["jpg", "jpeg"])
    if upload_file is not None:
        predict_from_upload_file(upload_file)


def predict_from_upload_file(upload_file: UploadedFile):
    with tempfile.NamedTemporaryFile(suffix=".jpg") as tmp_file:
        tmp_file.write(upload_file.getvalue())
        predict, img = get_predict(pathlib.Path(tmp_file.name))

    st.image(img)
    predict_text = f"Predicted {predict} "
    if predict == "dog":
        predict_text += "🐶"
    elif predict == "cat":
        predict_text += "😼"

    st.header(predict_text)


if __name__ == "__main__":
    index()
