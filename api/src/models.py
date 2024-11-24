from pydantic import BaseModel, Field

class InputData(BaseModel):
    gender: str = Field(..., description="Género (male o female)")
    height: int = Field(..., ge=0, description="Estatura en cm")
    weight: int = Field(..., ge=0, description="Peso en kg")
    physical_activity_level: str = Field(..., description="Nivel de actividad física (Baja, Media, Alta)")
    smoking_status: str = Field(..., description="Estado de fumador (No fuma, Fuma poco, Fuma frecuentemente)")
    cognitive_function: int = Field(..., ge=0, le=100, description="Función cognitiva (0 a 100)")
    mental_health_status: str = Field(..., description="Estado de salud mental (Malo, Intermedio, Bueno, Excelente)")
    sleep_patterns: str = Field(..., description="Patrones de sueño (Insomnio, Normal, Excesivo)")
    income_level: str = Field(..., description="Nivel de ingresos (Bajo, Medio, Alto)")
    sun_exposure: int = Field(..., ge=0, le=10, description="Exposición al sol (0 a 10)")
    pollution_exposure: int = Field(..., ge=0, le=10, description="Exposición a contaminación (0 a 10)")
    stress_levels: int = Field(..., ge=0, le=10, description="Nivel de estrés (0 a 10)")
    diet: str = Field(..., description="Dieta (Balanceada, Alta en grasas, etc.)")

class OutputData(BaseModel):
    age_prediction: float = Field(..., description="Predicción de edad en años")  