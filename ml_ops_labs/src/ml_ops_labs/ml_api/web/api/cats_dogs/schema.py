from pydantic import BaseModel
from ml_ops_labs.ml_api.web.api.cats_dogs.model import PetT


class DetectPetResponse(BaseModel):
    predict: PetT
