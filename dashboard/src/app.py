import pandas              as pd
import numpy               as np
import matplotlib.pyplot   as plt
import seaborn as sns
from matplotlib.lines import Line2D
import streamlit as st

df = pd.read_csv('data\Train.csv')
tabla = pd.set_option('display.max_columns', None)
df.head(5)



df[['Height (cm)',
 'Weight (kg)',
 'Cholesterol Level (mg/dL)',
 'BMI',
 'Blood Glucose Level (mg/dL)',
 'Hearing Ability (dB)',
 'Cognitive Function',
 'Stress Levels',
 'Pollution Exposure',
 'Sun Exposure',
 'Age (years)']] = df[['Height (cm)',
 'Weight (kg)',
 'Cholesterol Level (mg/dL)',
 'BMI',
 'Blood Glucose Level (mg/dL)',
 'Hearing Ability (dB)',
 'Cognitive Function',
 'Stress Levels',
 'Pollution Exposure',
 'Sun Exposure',
 'Age (years)']].round(0)

df[['Height (cm)',
 'Weight (kg)',
 'Cholesterol Level (mg/dL)',
 'BMI',
 'Blood Glucose Level (mg/dL)',
 'Hearing Ability (dB)',
 'Cognitive Function',
 'Stress Levels',
 'Pollution Exposure',
 'Sun Exposure',
 'Age (years)']].astype(int)  

column_list = list(df.columns)
titulos_columnas = pd.DataFrame(df.columns, columns=['Data'])

df['Rango edad'] = df['Age (years)'].apply(lambda valor: '18-20' if valor <= 20 else
                                                         '21-29' if 21 <= valor <= 29 else
                                                         '30-39' if 30 <= valor <= 39 else
                                                         '40-49' if 40 <= valor <= 49 else
                                                         '50-59' if 50 <= valor < 60 else 'mayor a 60')

df['Rango peso'] = df['Weight (kg)'].apply(lambda valor: '33 - 45' if valor <= 45.0 else
                                                         '46 - 59' if 46 <= valor <= 59 else
                                                         '60 - 79' if 60 <= valor <= 79 else
                                                         '80 - 89' if 80 <= valor <= 89 else
                                                         '90 - 100' if 90 <= valor <= 100 else 'mayor a 100')


df['Nivel de estres'] = df['Stress Levels'].apply(lambda valor: 'Bajo' if valor <= 3 else
                                                                'Medio' if 4 <= valor <= 6 else 'Alto')

def plot_dist_chart (grupo, nom_grupo, valor, color_graf, color_borde):
  df_graf = df.groupby(grupo).count().reset_index()
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

def fig_est_gen():
    df_hombres = df[df['Gender'] == 'Male']
    df_mujeres = df[df['Gender'] == 'Female']
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

def fig_edad_gen():
    df_hombres = df[df['Gender'] == 'Male']
    df_mujeres = df[df['Gender'] == 'Female']
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

def fig_estr_edad():
    df_estres_bajo = df[df['Nivel de estres'] == 'Bajo']
    df_estres_medio = df[df['Nivel de estres'] == 'Medio']
    df_estres_alto = df[df['Nivel de estres'] == 'Alto']
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




def main():
    
    APP_TITLE = "Data analysis based on various health and lifestyle factors"
    st.title(APP_TITLE)

    
    st.header("🗄 Base de datos", help="En esta seccion podra realizar una visualizacion de los datos que contiene la base de datos que esta consultando")
    st.write(df.head(5))      

    st.write("----")

    def data_segment():
        # Mostrar los datos (nombres de las columnas)
        st.header("📊 Datos", help="En esta seccion estan los nombres de los datos a analizar")
        st.write(titulos_columnas)

    def estadistica_segment():
        # Mostrar estadísticas descriptivas
        st.header("📈 Estadísticas descriptivas", help="En esta seccion puede visualizar un resumen de las estadisticas de la base de datos")
        st.write(df.describe())


    # Crear barra lateral para seleccionar el tipo de gráfico y filtrar datos
    def distr_segment():
        st.header("📈 Visualizacion de graficos de distribucion", help="En esta seccion puede visualizar graficos de distribucion de distintas categorias")

        chart_type = st.selectbox(
        "Selecciona los datos de la distribucion:",
        ["Por genero", "Por rango de edad", "Por rango de peso", "Por nivel de estres"])

        if chart_type == "Por genero":
            st.subheader("distribución de datos por genero:")
            fig = plot_dist_chart ('Gender','el genero','Height (cm)', '#87ceeb','black')
            #sns.scatterplot(fig)
            st.pyplot(fig)

        elif chart_type == "Por rango de edad":
            st.subheader("distribución de datos por rango de edad")
            fig2 = plot_dist_chart ('Rango edad','el rango de edades','Height (cm)', '#ffff00','black')
            #sns.scatterplot(fig2)
            st.pyplot(fig2)
            
        elif chart_type == "Por rango de peso":
            st.subheader("distribución de datos por rango de peso")
            fig3 = plot_dist_chart ('Rango peso','el rango de peso','Height (cm)', '#00ff00','black')
            #sns.scatterplot(fig3)
            st.pyplot(fig3)

        elif chart_type == "Por rango de peso":
            st.subheader("distribución de datos por nivel de estres")
            fig4 = plot_dist_chart ('Nivel de estres','el nivel de estres','Height (cm)','#ffa500','black')
            #sns.scatterplot(fig4)
            st.pyplot(fig4)

    def distr_segment2():
        st.header("📈 Visualizacion de graficos de distribucion por agrupacion", help="En esta seccion puede visualizar graficos de distribucion de distintas categorias agrupadas por otras categorias")

        chart_type = st.selectbox(
        "Selecciona los datos de la distribucion:",
        ["Por genero y nivel de estres", "Por rango de edad y genero", "Por nivel de estres y edad"])

        if chart_type == "Por genero y nivel de estres":
            st.subheader("distribución de datos por genero y nivel de estres:")
            fig = fig_est_gen()
            #sns.scatterplot(fig)
            st.pyplot(fig)

        elif chart_type == "Por rango de edad y genero":
            st.subheader("distribución de datos por rango de edad y genero")
            fig2 = fig_edad_gen()
            #sns.scatterplot(fig2)
            st.pyplot(fig2)
            
        elif chart_type == "Por nivel de estres y edad":
            st.subheader("distribución de datos por nivel de estres y edad")
            fig3 = fig_estr_edad()
            #sns.scatterplot(fig3)
            st.pyplot(fig3)        


  
    st.sidebar.title("🧬 Data analysis based on various health and lifestyle factors")
    st.sidebar.subheader("⚙️ Opciones")

    

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
    #"🗃 schema": schema_segment,
    #"🔎 view": view_segment,
    #"📸 materialized view": materialized_view_segment,
    #"🚉 stage": stage_segment,
    #"🚰 pipe": pipe_segment,
    #"🚚 data loading": data_loading_segment,
    #"📋 task": task_segment,
    #"🌊 stream": stream_segment,
    #"🪄 function": function_segment,
    #"🪜 procedure": procedure_segment,
    #"🔄 dynamic table": dynamic_table_segment,
    #"🚨 alert": alert_segment,
    #"🌀 data manipulation": data_manipulation_segment"
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
        distr_segment()
    elif selected_api == "Distribucion por multiples categorias":
        distr_segment2()




if __name__ == "__main__":
    #  Esto se usa para ejecutar la función main() directamente desde este archivo
    main()
