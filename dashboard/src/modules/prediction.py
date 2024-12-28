import streamlit as st
import pandas as pd

def predict_age():
    st.header("Predicción de Edad")
    
    # Inputs de usuario
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


    # Preparar datos para el modelo
    input_data = pd.DataFrame({
        'Gender': [1 if Gender == "male" else 0],
        'Height (cm)': [Height],
        'Weight (kg)': [Weight],
        'Physical Activity Level': [1 if Physical_Activity_Level == "Baja" else 2 if Physical_Activity_Level == "Media" else 0],
        'Smoking Status': [2 if Smoking_Status == "No fuma" else 1 if Smoking_Status == "Fuma poco" else 0 ],
        'Diet': [3 if Diet == "Vegetatiana" else 2 if Diet == "Baja en carboidratos" else 1 if Diet == "Alta en grasas" else 0],
        'Cognitive Function': [Cognitive_Function],
        'Mental Health Status': [3 if Mental_Health_Status == "Malo" else 1 if Mental_Health_Status == "Intermedio" else 2 if Mental_Health_Status == "Bueno" else 0],
        'Sleep Patterns': [1 if Sleep_Patterns == "Insomnio" else 2 if Sleep_Patterns == "Normal" else 0],
        'Stress Levels': [Stress_Levels],
        'Pollution Exposure': [Pollution_Exposure],
        'Sun Exposure': [Sun_Exposure],
        'Income Level': [1 if Income_Level == "Bajo" else 2 if Income_Level == "Medio" else 0]        
         })
    
    # Predicción
    #if st.button("Hacer Predicción"):
    #    prediction = model.predict(input_data)[0]
    #    st.write(f"Resultado de la predicción: **{prediction}**")


    if st.button("Hacer Predicción"):
        response = requests.post(url, json = predict)
        prediction = response.json()

        if response.status_code == 200:
            st.write(f"Resultado de la predicción: **{prediction} años**")
        else:
            st.error(f"Error al realizar la predicción: {response.status_code}")

   # request.post hacer el post con un diccionario          