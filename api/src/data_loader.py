import os
import pandas as pd
import joblib
import streamlit as st
from pathlib import Path


DEFAULT_DATA_PATH = Path(__file__).parent.parent.parent/'data/Train.csv'
DEFAULT_MODEL_PATH = Path(__file__).parent.parent.parent/'src/models/gaussian_model.joblib'

@st.cache_data
def load_data():
    data_path = os.getenv("HEALTH_DATA_PATH", DEFAULT_DATA_PATH)    
    return pd.read_csv(data_path)

@st.cache_data
def load_model():
    model_path = os.getenv("HEALTH_MODEL_PATH", DEFAULT_MODEL_PATH)
    return joblib.load(model_path)



