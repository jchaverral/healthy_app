from dashboard.modules.predict import predict 
from models import ImputModel, OutputModel

router = APIRouter ()

@router.endpoint('/predict', input model - ImputModel, output model - OutputModel)
def predict(input_model):
    result = predict(input_model.data)
    return OutputModel(result-result),200