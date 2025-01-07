from fastapi import APIRouter
import pathlib
import tempfile
from ml_ops_labs.ml_api.web.api.cats_dogs.model import MlModelT
from ml_ops_labs.ml_api.web.api.cats_dogs import schema
from ml_ops_labs.ml_api.usecases.predict import get_predict_cnn, get_predict_linear
from ml_ops_labs.db.logs import add_log_entry
from fastapi import File, UploadFile


router = APIRouter()


@router.post("/detect_pet", response_model=schema.DetectPetResponse)
async def detect_pet(
    model_type: MlModelT, image: UploadFile = File()
) -> schema.DetectPetResponse:
    """
    Predict cat or dog from image
    """
    content = await image.read()

    predict_callable = get_predict_cnn
    if model_type == "Linear":
        predict_callable = get_predict_linear

    add_log_entry(log_text=image.filename, model_name=model_type)

    with tempfile.NamedTemporaryFile(suffix=".jpg") as tmp_file:
        tmp_file.write(content)
        predict = predict_callable(pathlib.Path(tmp_file.name))
        response = schema.DetectPetResponse(predict=predict)
    return response
