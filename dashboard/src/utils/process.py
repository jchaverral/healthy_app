import pandas              as pd
import numpy               as np
import matplotlib.pyplot   as plt
import seaborn as sns
from matplotlib.lines import Line2D


from utils.process_utils import round_data, convert_to_int

def process_data_mod(df):
    columns_round = ['Height (cm)',
    'Weight (kg)',
    'Cholesterol Level (mg/dL)',
    'BMI',
    'Blood Glucose Level (mg/dL)',
    'Hearing Ability (dB)',
    'Cognitive Function',
    'Stress Levels',
    'Pollution Exposure',
    'Sun Exposure',
    'Age (years)']

    columns_type = ['Height (cm)',
    'Weight (kg)',
    'Cholesterol Level (mg/dL)',
    'BMI',
    'Blood Glucose Level (mg/dL)',
    'Hearing Ability (dB)',
    'Cognitive Function',
    'Stress Levels',
    'Pollution Exposure',
    'Sun Exposure',
    'Age (years)']
    
    df = round_data(df,columns_round, round_number=0)
    df = convert_to_int(df,columns_type,type_col=int)

    return df

def process_data(df):

    df_ = process_data_mod(df)
  

    df_['Rango edad'] = df_['Age (years)'].apply(lambda valor: '18-20' if valor <= 20 else
                                                         '21-29' if 21 <= valor <= 29 else
                                                         '30-39' if 30 <= valor <= 39 else
                                                         '40-49' if 40 <= valor <= 49 else
                                                         '50-59' if 50 <= valor < 60 else 'mayor a 60')

    df_['Rango peso'] = df_['Weight (kg)'].apply(lambda valor: '33 - 45' if valor <= 45.0 else
                                                            '46 - 59' if 46 <= valor <= 59 else
                                                            '60 - 79' if 60 <= valor <= 79 else
                                                            '80 - 89' if 80 <= valor <= 89 else
                                                            '90 - 100' if 90 <= valor <= 100 else 'mayor a 100')


    df_['Nivel de estres'] = df_['Stress Levels'].apply(lambda valor: 'Bajo' if valor <= 3 else
                                                                    'Medio' if 4 <= valor <= 6 else 'Alto')
    

    return df_







