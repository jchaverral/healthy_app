from fastapi import FastAPI
from pydantic import BaseModel
from predict import load_model
from routes import api_router

model = load_model()

app = FastAPI(
    title="Modelo de Predicción de Edad",
    description="API para predecir la edad basada en características físicas y de estilo de vida."
)


app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

#FastAPI se encarga de gestionar las solicitudes HTTP.
#api_router organiza las rutas desde routes.py.
#uvicorn ejecuta el servidor.    
