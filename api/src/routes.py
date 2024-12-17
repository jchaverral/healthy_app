from fastapi import APIRouter
from models import InputData, OutputData
from predict import predict


api_router = APIRouter()

@api_router.post('/predict/', response_model= OutputData)
def predict_model(input_model:InputData):
    result = predict(input_model)
    response = OutputData(age_prediction=result)
    return response