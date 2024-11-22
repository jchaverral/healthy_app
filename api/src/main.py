import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from modules.data_loader import load_model


model = load_model()

app = FastAPI()

