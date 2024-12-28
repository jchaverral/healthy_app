import numpy               as np
import matplotlib.pyplot   as plt

from utils.process import process_data


def plot_dist_chart (df, grupo, nom_grupo, valor, color_graf, color_borde):
  df_= process_data(df)
  df_graf = df_.groupby(grupo).count().reset_index()
  categorias = df_graf[grupo]
  valores = df_graf[valor]
  x = np.arange(len(categorias))
  fig = plt.figure()
  plt.bar(x, valores, color = color_graf, edgecolor=color_borde, alpha=0.75)
  plt.title(f'distribución de datos por {nom_grupo}', fontsize=12, fontweight='bold', pad=20)
  plt.xlabel(f'{grupo}', fontsize=10)
  plt.ylabel('Cantidad', fontsize=10)
  for i in range(len(categorias)):
      plt.text(x[i], valores[i]+0.5, str(valores[i]),  rotation=90, ha='center', va='bottom', fontsize=10, color='black')
  plt.xticks(x, categorias, ha='center')
  plt.grid(axis='y', linestyle='--', alpha=0.7)
  return fig

def plot_height_gender(df):
    df_= process_data(df)
    df_hombres = df_[df_['Gender'] == 'Male']
    df_mujeres = df_[df_['Gender'] == 'Female']
    df_grup_hombres = df_hombres.groupby('Nivel de estres').count().reset_index()
    df_grup_mujeres = df_mujeres.groupby('Nivel de estres').count().reset_index()
    categorias1 = df_grup_hombres ['Nivel de estres']
    valores1 = df_grup_hombres['Height (cm)']
    categorias2 = df_grup_mujeres['Nivel de estres']
    valores2 = df_grup_mujeres['Height (cm)']
    x = np.arange(len(categorias2))
    fig = plt.figure()
    width = 0.35
    plt.bar(x - width/2, valores1, width, label='Hombres', color = '#87ceeb', edgecolor='black', alpha=0.75)
    plt.bar(x + width/2, valores2, width, label='Mujeres', color = '#ffb6c1', edgecolor='black', alpha=0.75)
    plt.title('Nivel de estres segun el genero', fontsize=12, fontweight='bold', pad=20)
    #plt.xlabel(f'{grupo}', fontsize=10)
    plt.ylabel('Cantidad', fontsize=10)
    for i in range(len(categorias1)):
        plt.text(x[i]- width/2, valores1[i]+0.5, str(valores1[i]),  rotation=90, ha='center', va='bottom', fontsize=10, color='black')
    for i in range(len(categorias2)):
        plt.text(x[i]+ width/2, valores2[i]+0.5, str(valores2[i]),  rotation=90, ha='center', va='bottom', fontsize=10, color='black')
    plt.xticks(x, categorias1, ha='center')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
    return fig

def plot_age_gender(df):
    df_= process_data(df)
    df_hombres = df_[df_['Gender'] == 'Male']
    df_mujeres = df_[df_['Gender'] == 'Female']
    df_grup_hombres = df_hombres.groupby('Rango edad').count().reset_index()
    df_grup_mujeres = df_mujeres.groupby('Rango edad').count().reset_index()
    categorias1 = df_grup_hombres ['Rango edad']
    valores1 = df_grup_hombres['Height (cm)']
    categorias2 = df_grup_mujeres['Rango edad']
    valores2 = df_grup_mujeres['Height (cm)']
    x = np.arange(len(categorias2))
    fig = plt.figure()
    width = 0.35
    plt.bar(x - width/2, valores1, width, label='Hombres', color = '#87ceeb', edgecolor='black', alpha=0.75)
    plt.bar(x + width/2, valores2, width, label='Mujeres', color = '#ffb6c1', edgecolor='black', alpha=0.75)
    plt.title('Rango de edades segun el genero', fontsize=12, fontweight='bold', pad=20)
    #plt.xlabel(f'{grupo}', fontsize=10)
    plt.ylabel('Cantidad', fontsize=10)
    for i in range(len(categorias1)):
        plt.text(x[i]- width/2, valores1[i]+0.5, str(valores1[i]),  rotation=90, ha='center', va='bottom', fontsize=10, color='black')
    for i in range(len(categorias2)):
        plt.text(x[i]+ width/2, valores2[i]+0.5, str(valores2[i]),  rotation=90, ha='center', va='bottom', fontsize=10, color='black')
    plt.xticks(x, categorias1, ha='center')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
    return fig

def plot_stress_age(df):
    df_= process_data(df)
    df_estres_bajo = df_[df_['Nivel de estres'] == 'Bajo']
    df_estres_medio = df_[df_['Nivel de estres'] == 'Medio']
    df_estres_alto = df_[df_['Nivel de estres'] == 'Alto']
    df_grup_bajo = df_estres_bajo.groupby('Rango edad').count().reset_index()
    df_grup_medio = df_estres_medio.groupby('Rango edad').count().reset_index()
    df_grup_alto = df_estres_alto.groupby('Rango edad').count().reset_index()
    categorias1 = df_grup_bajo['Rango edad']
    valores1 = df_grup_bajo['Height (cm)']
    categorias2 = df_grup_medio['Rango edad']
    valores2 = df_grup_medio['Height (cm)']
    categorias3 = df_grup_alto['Rango edad']
    valores3 = df_grup_alto['Height (cm)']
    fig = plt.figure()
    x = np.arange(len(categorias2))
    width = 0.2
    plt.bar(x - width, valores1, width, label='Bajo', color = '#ffff00', edgecolor='black', alpha=0.75)
    plt.bar(x, valores2, width, label='Medio', color = '#ffa500', edgecolor='black', alpha=0.75)
    plt.bar(x + width, valores3, width, label='Alto', color = '#ff0000', edgecolor='black', alpha=0.75)
    plt.title('Nivel de estres segun el rango de edades', fontsize=12, fontweight='bold', pad=20)
    #plt.xlabel(f'{grupo}', fontsize=10)
    plt.ylabel('Cantidad', fontsize=10)
    for i in range(len(categorias1)):
        plt.text(x[i]- width, valores1[i]+0.5, str(valores1[i]),  rotation=90, ha='center', va='bottom', fontsize=10, color='black')
    for i in range(len(categorias2)):
        plt.text(x[i], valores2[i]+0.5, str(valores2[i]),  rotation=90, ha='center', va='bottom', fontsize=10, color='black')
    for i in range(len(categorias2)):
        plt.text(x[i]+ width, valores3[i]+0.5, str(valores3[i]),  rotation=90, ha='center', va='bottom', fontsize=10, color='black')
    plt.xticks(x, categorias1, ha='center')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()
    return fig    