import pandas as pd
import sqlite3

# Leer el archivo Excel original
df = pd.read_excel("reactiva.xlsx",header= 1)
print(df.columns)
def limpiar_y_renombrar_columnas(df):
    # Renombrar columnas eliminando espacios, tildes y convirtiendo a minúsculas
    df.columns = df.columns.str.lower().str.replace(' ', '_').str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

    # Eliminar columna ID y TipoMoneda duplicada
    df = df.loc[:, ~df.columns.duplicated()]

    df.columns = df.columns.str.replace('_', ' ')
    df = df.rename(columns={'dispositivo 2': 'dispositivo legal', 'estado  ssp': 'estado'})
    print(df.columns)
import pandas as pd
import requests

# Definir la URL del API de Sunat
url = "https://api.apis.net.pe/v1/tipo-cambio-sunat?month=3&year=2024"

# Obtener los datos del tipo de cambio del API de Sunat
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    
    # Obtener el último tipo de cambio
    tipo_cambio = data[-1]['venta']  # Suponiendo que el último tipo de cambio es el más reciente
    print("Tipo de cambio obtenido:", tipo_cambio)
# Agregar la columna 'moneda de cambio' con el valor 'USD'
df['moneda de cambio'] = 'USD'
 # Convertir el monto de inversión de soles a dólares utilizando el tipo de cambio
df['monto de inversion en dolares'] = df['monto de inversion'] / tipo_cambio

    # Mostrar las primeras filas del DataFrame con las nuevas columnas
print(df.columns)
print (df.head())
