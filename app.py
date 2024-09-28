#Importa las bibliotecas necesarias:
import streamlit as st
import pandas as pd

#Crea un título para la aplicación:
st.title("Visualizador de Datos CSV")

#Crea un widget de carga de archivos:
uploaded_file = st.file_uploader("Sube un archivo CSV", type=["csv"])

#Verifica si se ha cargado un archivo:
if uploaded_file is not None:
    # Lee el archivo CSV en un DataFrame de Pandas
    df = pd.read_csv(uploaded_file)

#Muestra el DataFrame como una tabla:
st.table(df)