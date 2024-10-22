import requests
import sqlite3
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017/')
mongo_db = client['sunat_database']
mongo_collection = mongo_db['sunat_info']

# Conectar a SQLite
conn = sqlite3.connect('base.db')
cursor = conn.cursor()

# Crear la tabla sunat_info en SQLite si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS sunat_info (
        fecha TEXT PRIMARY KEY,
        compra REAL,
        venta REAL
    )
''')

url = "https://api.apis.net.pe/v1/tipo-cambio-sunat"

def obtener_tipo_cambio():
    datos_2023 = []
    for mes in range(1, 13): 
        params = {
            "year": 2023,
            "month": mes
        }
        # Realizar la solicitud a la API
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            datos_2023.extend(data) 

    return datos_2023
datos_tipo_cambio = obtener_tipo_cambio()

for dato in datos_tipo_cambio:
    fecha = dato['fecha']
    compra = float(dato['compra'])
    venta = float(dato['venta'])
    cursor.execute('''
        INSERT OR IGNORE INTO sunat_info (fecha, compra, venta)
        VALUES (?, ?, ?)
    ''', (fecha, compra, venta))
    mongo_document = {
        'fecha': fecha,
        'compra': compra,
        'venta': venta
    }
    mongo_collection.insert_one(mongo_document)

conn.commit()
cursor.execute('SELECT * FROM sunat_info')
resultados = cursor.fetchall()

for fila in resultados:
    print(fila)

conn.close()
