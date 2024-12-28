import pandas as pd
import joblib
from pathlib import Path
import os
from models import InputData




DEFAULT_MODEL_PATH = Path(__file__).parent/'ml_models/gaussian_model.joblib'
def load_model():
    model_path = os.getenv("HEALTH_MODEL_PATH", DEFAULT_MODEL_PATH)
    return joblib.load(model_path)


def process_data(input_data: InputData) -> pd.DataFrame:
    """
    Preprocesa los datos de entrada para que sean compatibles con el modelo.
    """
    data = {
        'Gender': [1 if input_data.gender == "male" else 0],
        'Height (cm)': [input_data.height],
        'Weight (kg)': [input_data.weight],
        'Physical Activity Level': [1 if input_data.physical_activity_level == "Baja" else 
                                    2 if input_data.physical_activity_level == "Media" else 0],
        'Smoking Status': [2 if input_data.smoking_status == "No fuma" else 
                           1 if input_data.smoking_status == "Fuma poco" else 0],
        'Diet': [3 if input_data.diet == "Vegetariana" else 
                 2 if input_data.diet == "Baja en carbohidratos" else 
                 1 if input_data.diet == "Alta en grasas" else 0],
        'Cognitive Function': [input_data.cognitive_function],
        'Mental Health Status': [3 if input_data.mental_health_status == "Malo" else 
                                 1 if input_data.mental_health_status == "Intermedio" else 
                                 2 if input_data.mental_health_status == "Bueno" else 0],
        'Sleep Patterns': [1 if input_data.sleep_patterns == "Insomnio" else 
                           2 if input_data.sleep_patterns == "Normal" else 0],
        'Stress Levels': [input_data.stress_levels],
        'Pollution Exposure': [input_data.pollution_exposure],
        'Sun Exposure': [input_data.sun_exposure],
        'Income Level': [1 if input_data.income_level == "Bajo" else 
                         2 if input_data.income_level == "Medio" else 0]
    }
    return pd.DataFrame(data)

def predict(input_data: InputData) -> float:
    model = load_model()
    df = process_data(input_data)
    prediction = model.predict(df)[0]
    return prediction



