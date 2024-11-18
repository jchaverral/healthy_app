from modules.data_loader import load_model
from modules.prediction import predict_age

model = load_model()
predict_age(model)