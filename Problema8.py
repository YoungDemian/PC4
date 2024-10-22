import csv
import sqlite3
conn = sqlite3.connect('base.db')
cursor = conn.cursor()
def obtener_tipo_cambio(fecha):
    cursor.execute('''
        SELECT compra, venta FROM sunat_info WHERE fecha = ?
    ''', (fecha,))
    resultado = cursor.fetchone()
    if resultado:
        return resultado[0], resultado[1] 
    else:
        return None, None 
with open('ventas.csv', newline='') as csvfile:
    lector = csv.DictReader(csvfile)
    resultados = []
    
    for fila in lector:
        producto = fila['producto']
        fecha_compra = fila['fecha_compra']
        precio_dolar = float(fila['precio_dolar'])
        compra, venta = obtener_tipo_cambio(fecha_compra)
        
        if compra is not None:
            precio_soles = precio_dolar * compra
            resultados.append({
                'producto': producto,
                'precio_dolar': precio_dolar,
                'precio_soles': precio_soles
            })
        else:
            print(f"No se encontró tipo de cambio para la fecha {fecha_compra}")
for resultado in resultados:
    print(f"Producto: {resultado['producto']}, Precio en dólares: {resultado['precio_dolar']:.2f}, Precio en soles: {resultado['precio_soles']:.2f}")
conn.close()
