import streamlit as st
from PIL import Image
from streamlit.runtime.uploaded_file_manager import UploadedFile
from pathlib import Path
import tempfile
from ml_ops_labs.clients.ml_api import predict_pet


def index() -> None:
    st.title("Cats VS Dogs classifier")
    upload_file = st.file_uploader(label="Upload image", type=["jpg", "jpeg"])
    if upload_file is not None:
        predict_from_upload_file(upload_file)


def predict_from_upload_file(upload_file: UploadedFile):
    with tempfile.NamedTemporaryFile(suffix=".jpg") as tmp_file:
        tmp_file.write(upload_file.getvalue())
        predict = predict_pet(model_type="Linear", file_path=Path(tmp_file.name))
        pil_img = Image.open(tmp_file)
        st.image(pil_img)
    # predict = detect_pet(client=client, body=BodyDetectPetApiCatsDogsDetectPetPost(image=))
    predict_text = f"Predicted {predict} "
    if predict == "dog":
        predict_text += "🐶"
    elif predict == "cat":
        predict_text += "😼"

    st.header(predict_text)


if __name__ == "__main__":
    index()
