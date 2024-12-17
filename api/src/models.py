from pydantic import BaseModel

class InputData(BaseModel):
    gender: str 
    height: int 
    weight: int 
    physical_activity_level: str 
    smoking_status: str
    diet: str 
    cognitive_function: int 
    mental_health_status: str 
    sleep_patterns: str 
    stress_levels: int  
    pollution_exposure: int 
    sun_exposure: int
    income_level: str 

class OutputData(BaseModel):
    age_prediction: float 