import streamlit as st
import pandas as pd
import requests
from predict import predict

def predict_age():
    url = 'http://127.0.0.1:8000/predict/'


    st.header("Predicción de Edad")
    st.subheader("Introduce los datos de la persona para hacer una predicción")

    Height = st.number_input("Estatura (cm)", 0, 200)
    Weight = st.number_input("Peso (kg)", 0, 130)
    Gender = st.selectbox("Genero", ["male", "female"])
    Physical_Activity_Level = st.selectbox("Nivel de actividad fisica", ["Baja", "Media", "Alta"])
    Smoking_Status = st.selectbox("Es fumador, moderado o frecuente", ["No fuma", "Fuma poco", "Fuma frecuentemente"])
    Cognitive_Function = st.slider("Funcion cognitiva", 0, 100)
    Mental_Health_Status = st.selectbox("Estado de salud mental", ["Malo", "Intermedio", "Bueno","Excelente"])
    Sleep_Patterns = st.selectbox("Patrones de sueno", ["Insomnio", "Normal", "Excesivo"])
    Income_Level = st.selectbox("Niveles de ingreso", ["Bajo", "Medio", "Alto"])
    Sun_Exposure = st.slider("Exposicion al sol", 0, 10)
    Pollution_Exposure = st.slider("Exposicion a la pulucion/contaminacion", 0, 10)
    Stress_Levels = st.slider("Nivel de estres", 0, 10)
    Diet = st.selectbox("Dieta", ["Balanceada", "Alta en grasas", "Baja en carboidratos", "Vegetatiana"])



    if st.button("Hacer Predicción"):
        response = requests.post(url, json = predict)
        prediction = response.json()

        if response.status_code == 200:
            st.write(f"Resultado de la predicción: **{prediction} años**")
        else:
            st.error(f"Error al realizar la predicción: {response.status_code}")


if __name__ == "__main__":
    predict_age()