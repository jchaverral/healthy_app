import pandas              as pd
import numpy               as np
import matplotlib.pyplot   as plt
import seaborn as sns
from matplotlib.lines import Line2D
import streamlit as st
from modules.information_graphics import plot_dist_chart, plot_height_gender,plot_age_gender, plot_stress_age


# Crear barra lateral para seleccionar el tipo de gráfico y filtrar datos
def plot_distr_segment(df):
    st.header("📈 Visualizacion de graficos de distribucion", help="En esta seccion puede visualizar graficos de distribucion de distintas categorias")

    chart_type = st.selectbox(
    "Selecciona los datos de la distribucion:",
    ["Por genero", "Por rango de edad", "Por rango de peso", "Por nivel de estres"])

    if chart_type == "Por genero":
        st.subheader("distribución de datos por genero:")
        fig = plot_dist_chart (df,'Gender','el genero','Height (cm)', '#87ceeb','black')
        #sns.scatterplot(fig)
        st.pyplot(fig)

    elif chart_type == "Por rango de edad":
        st.subheader("distribución de datos por rango de edad")
        fig2 = plot_dist_chart (df,'Rango edad','el rango de edades','Height (cm)', '#ffff00','black')
        #sns.scatterplot(fig2)
        st.pyplot(fig2)
        
    elif chart_type == "Por rango de peso":
        st.subheader("distribución de datos por rango de peso")
        fig3 = plot_dist_chart (df,'Rango peso','el rango de peso','Height (cm)', '#00ff00','black')
        #sns.scatterplot(fig3)
        st.pyplot(fig3)

    elif chart_type == "Por rango de peso":
        st.subheader("distribución de datos por nivel de estres")
        fig4 = plot_dist_chart (df,'Nivel de estres','el nivel de estres','Height (cm)','#ffa500','black')
        #sns.scatterplot(fig4)
        st.pyplot(fig4)

def plot_distr_segment2(df):
    st.header("📈 Visualizacion de graficos de distribucion por agrupacion", help="En esta seccion puede visualizar graficos de distribucion de distintas categorias agrupadas por otras categorias")

    chart_type = st.selectbox(
    "Selecciona los datos de la distribucion:",
    ["Por genero y nivel de estres", "Por rango de edad y genero", "Por nivel de estres y edad"])

    if chart_type == "Por genero y nivel de estres":
        st.subheader("distribución de datos por genero y nivel de estres:")
        fig = plot_height_gender(df)
        #sns.scatterplot(fig)
        st.pyplot(fig)

    elif chart_type == "Por rango de edad y genero":
        st.subheader("distribución de datos por rango de edad y genero")
        fig2 = plot_age_gender(df)
        #sns.scatterplot(fig2)
        st.pyplot(fig2)
        
    elif chart_type == "Por nivel de estres y edad":
        st.subheader("distribución de datos por nivel de estres y edad")
        fig3 = plot_stress_age(df)
        #sns.scatterplot(fig3)
        st.pyplot(fig3)    
