import pandas              as pd
import numpy               as np
import matplotlib.pyplot   as plt
import seaborn as sns
from matplotlib.lines import Line2D
import streamlit as st
from utils.process_general_data import data_segment, estadistica_segment


#def display_analysis(df)
def display_general(df):
    
    data_segment(df)

    st.write("----")

    estadistica_segment(df)


        
