Actividad 2: Visualización de Datos con Pandas y Streamlit
Objetivo: Crear una aplicación web simple utilizando Streamlit para cargar un archivo CSV, procesarlo con Pandas y mostrar la información en una tabla.

Entorno Virtual:

Crea un directorio para tu proyecto: mkdir mi-proyecto-streamlit
Navega al directorio: cd mi-proyecto-streamlit
Crea un entorno virtual: python3 -m venv .venv
Activa el entorno virtual: .venv\Scripts\activate (Windows) (copiar la rura desde Scripts)
Instala las librerías: pip install pandas streamlit
Pasos:

Crea el archivo app.py en el directorio del proyecto.

Importa las bibliotecas necesarias:
import streamlit as st
import pandas as pd

Crea un título para la aplicación:

Crea un widget de carga de archivos:

Verifica si se ha cargado un archivo:

Mostrar la tabla en Streamlit

Paso 4: Ejecutar la aplicación

Ejecuta la aplicación Streamlit: streamlit run app.py
Abre la aplicación web en el navegador: http://localhost:8501/