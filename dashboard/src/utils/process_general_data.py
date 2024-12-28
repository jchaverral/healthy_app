
import pandas              as pd
import streamlit as st


def data_segment(df):
    # Mostrar los datos (nombres de las columnas)
    st.header("📊 Datos", help="En esta seccion estan los nombres de los datos a analizar")
    titulos_columnas = pd.DataFrame(df.columns, columns=['Data'])
    st.write(titulos_columnas)

def estadistica_segment(df):
    # Mostrar estadísticas descriptivas
    st.header("📈 Estadísticas descriptivas", help="En esta seccion puede visualizar un resumen de las estadisticas de la base de datos")
    st.write(df.describe())
