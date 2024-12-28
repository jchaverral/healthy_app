import os
import pandas as pd
import streamlit as st
from pathlib import Path


DEFAULT_DATA_PATH = Path(__file__).parent.parent.parent/'data/Train.csv'

@st.cache_data
def load_data():
    data_path = os.getenv("HEALTH_DATA_PATH", DEFAULT_DATA_PATH)    
    return pd.read_csv(data_path)




