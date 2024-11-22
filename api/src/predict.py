import pandas as pd
import joblib
import streamlit as st



def load_data():
    return pd.read_csv('data/Train.csv')

def load_model():
    return joblib.load('src/models/gaussian_model.joblib')

def predict(datos):
    model = load_model()
    result = model.predict(datos)
    return result



