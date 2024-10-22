import requests
import zipfile
import os
def descargar_imagen(url, nombre_archivo):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(nombre_archivo, 'wb') as file:
                file.write(response.content)
            print(f"Imagen descargada como {nombre_archivo}")
        else:
            print(f"Error al descargar la imagen. Código de estado: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar la imagen: {e}")
def comprimir_imagen(nombre_archivo, nombre_zip):
    if os.path.exists(nombre_archivo):
        with zipfile.ZipFile(nombre_zip, 'w') as zipf:
            zipf.write(nombre_archivo)
            print(f"Imagen comprimida como {nombre_zip}")
    else:
        print(f"El archivo {nombre_archivo} no existe. No se puede comprimir.")
def descomprimir_zip(nombre_zip, ruta_destino):
    if os.path.exists(nombre_zip):
        with zipfile.ZipFile(nombre_zip, 'r') as zipf:
            zipf.extractall(ruta_destino)
            print(f"Archivo descomprimido en {ruta_destino}")
    else:
        print(f"El archivo zip {nombre_zip} no existe. No se puede descomprimir.")
url_imagen = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
nombre_imagen = "imagen_descargada.jpg"
nombre_zip = "imagen_comprimida.zip"
ruta_descompresion = "."
descargar_imagen(url_imagen, nombre_imagen)
comprimir_imagen(nombre_imagen, nombre_zip)
descomprimir_zip(nombre_zip, ruta_descompresion)
