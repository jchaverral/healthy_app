import pandas              as pd
import numpy               as np
import matplotlib.pyplot   as plt
import seaborn as sns
from matplotlib.lines import Line2D
from sklearn import model_selection, metrics, linear_model
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import cross_val_score, KFold
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import train_test_split, KFold
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C
import joblib
#from utils.process import process_data_mod


# Filtrar alertas (futurewarnings)
from warnings import simplefilter
simplefilter(action="ignore", category=FutureWarning)

df = pd.read_csv('../../data/Train.csv')

def round_data(df,columns_round,round_number=0):
    _df = df.copy()
    _df[columns_round] = _df[columns_round].round(round_number)
    return _df

def convert_to_int(df,columns_type,type_col=int):
    _df = df.copy()
    _df[columns_type] = _df[columns_type].astype(type_col)  
    return _df

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


df = process_data_mod(df)

#elimino las columnas poco relevantes para este analisis
df_limpio = df.copy().drop(['Alcohol Consumption', 'Chronic Diseases','Medication Use', 'Family History', 'Education Level', 'Blood Pressure (s/d)', 'BMI', 'Blood Glucose Level (mg/dL)', 'Bone Density (g/cm²)', 'Cholesterol Level (mg/dL)', 'Vision Sharpness', 'Hearing Ability (dB)'], axis=1)

# transformar columnas tipo str en categoricas(numericas)
le = LabelEncoder()

columnas_trans = ['Gender', 'Physical Activity Level', 'Smoking Status', 'Mental Health Status', 'Diet', 'Sleep Patterns', 'Income Level']

for columna in columnas_trans:
  df_limpio[columna] = le.fit_transform(df_limpio[columna])


plt.figure(figsize=(10, 8))
sns.heatmap(df_limpio.corr(), annot=True, fmt=".2f", cmap='coolwarm', square=True)
plt.title('Matriz de Correlación')
plt.show()


mean = df_limpio.mean()
std_dev = df_limpio.std()

# Filtra los datos que estén dentro de un cierto número de desviaciones estándar
num_std_dev = 2  # Por ejemplo, 3 desviaciones estándar
df_limpio2 = df_limpio[(df_limpio >= mean - num_std_dev * std_dev) & (df_limpio <= mean + num_std_dev * std_dev)].dropna()
# MODELO
# Cargar el conjunto de datos
X = df_limpio2.drop('Age (years)', axis=1)
y = df_limpio2['Age (years)']

# Crear el kernel para el proceso gaussiano
kernel = C(1.0) * RBF(length_scale=1.0)

# Crear el modelo de Proceso Gaussiano
gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=10)

# Entrenar el modelo
gp.fit(X, y)

# Realizar predicciones
y_pred, y_std = gp.predict(X, return_std=True)

# Calcular el error cuadrático medio
mse = root_mean_squared_error(y, y_pred)
mae = mean_absolute_error(y, y_pred)
r2 = r2_score(y, y_pred)

print(f"MSE: {mse}")
print(f"MAE: {mae}")
print(f"R-squared: {r2}")

# Crear un DataFrame con y real y y predicho
resultados = pd.DataFrame({
    'y_real': y,
    'y_predicho': y_pred,
    'std_pred': y_std
})


#y_pred = gp.predict(X)

# Mostrar resultados
print(resultados)

#Guardamos el modelo en un archivo
joblib.dump(gp, "gaussian_model.joblib")
print("Modelo guardado como 'gaussian_model.joblib'")
