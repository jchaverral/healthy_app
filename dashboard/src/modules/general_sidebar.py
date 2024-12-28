import pandas              as pd
import numpy               as np
import matplotlib.pyplot   as plt
import seaborn as sns
from matplotlib.lines import Line2D
import streamlit as st
from modules.analysis import plot_distr_segment, plot_distr_segment2
from utils.process_general_data import data_segment, estadistica_segment



def general_sidebar(df):

    left_column_defaults = [
    "📊 Datos"
    #"📸 materialized view",
    #"🔄 dynamic table", 
    #"📋 task",
    #"🌊 stream",
    #"🚨 alert",
    ]

    right_column_defaults = [
        "📈 Estadísticas descriptivas"
        #"🚉 stage",
        #"🚚 data loading",
        #"🌀 data manipulation",
        #"🪄 function", 
        #"🪜 procedure",
        
        #"🚰 pipe",
        ]
    
    st.sidebar.title("🧬 Data analysis based on various health and lifestyle factors")
    st.sidebar.subheader("⚙️ Opciones")

    all_segments = left_column_defaults + right_column_defaults

    def default_layout():
        st.session_state["layout_left_column"] = left_column_defaults
        st.session_state["layout_right_column"] = right_column_defaults

    custom_layout = st.sidebar.expander("✏ Modifique la visualizacion")
    with custom_layout:
        st.button("Default Layout", on_click=default_layout)
        side_left_col, side_right_col = st.columns(2)
        left_col_segments = side_left_col.multiselect("Left Column", 
                            options=all_segments, 
                            default=left_column_defaults,
                            key="layout_left_column")
                            
        right_col_segments = side_right_col.multiselect("Right Column", 
                            options=all_segments, 
                            default=right_column_defaults,
                            key="layout_right_column")
    


    segment_dict = {
    "📊 Datos": data_segment,
    "📈 Estadísticas descriptivas": estadistica_segment
    }

    cols = st.columns(2)

    with cols[0]:
        for seg in left_col_segments:
            segment_dict[seg]()
        

    with cols[1]:
        for seg in right_col_segments:
            segment_dict[seg]()

    st.write("----")

    with st.sidebar:
        graficas = (
        "Distribucion por una categoria",
        "Distribucion por multiples categorias")
        selected_api = st.selectbox(
            label="🔎 Selecciona las graficas que deseas ver",
            options=graficas)
        
            
    if selected_api == "Distribucion por una categoria":
        plot_distr_segment()
    elif selected_api == "Distribucion por multiples categorias":
        plot_distr_segment2()