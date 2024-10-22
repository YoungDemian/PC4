import os

def solicitar_numero():
    while True:
        try:
            numero = int(input("Ingrese un número entre 1 y 10: "))
            if 1 <= numero <= 10:
                return numero
            else:
                print("El número debe estar entre 1 y 10. Intente nuevamente.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
def guardar_tabla(numero):
    nombre_archivo = f'tabla-{numero}.txt'
    with open(nombre_archivo, 'w') as archivo:
        for i in range(1, 11):
            archivo.write(f'{numero} x {i} = {numero * i}\n')
    print(f"Tabla de multiplicar del {numero} guardada en '{nombre_archivo}'.")
def mostrar_tabla(numero):
    nombre_archivo = f'tabla-{numero}.txt'
    try:
        with open(nombre_archivo, 'r') as archivo:
            print(f"Tabla de multiplicar del {numero}:")
            for linea in archivo:
                print(linea.strip())
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")
def mostrar_linea_tabla(numero, m):
    nombre_archivo = f'tabla-{numero}.txt'
    try:
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            if 1 <= m <= 10:
                print(f"Línea {m} de la tabla de multiplicar del {numero}: {lineas[m-1].strip()}")
            else:
                print("El número de línea debe estar entre 1 y 10.")
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")
def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Guardar tabla de multiplicar en un archivo")
        print("2. Mostrar tabla de multiplicar desde un archivo")
        print("3. Mostrar una línea específica de la tabla")
        print("4. Salir")
        
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            numero = solicitar_numero()
            guardar_tabla(numero)
        elif opcion == '2':
            numero = solicitar_numero()
            mostrar_tabla(numero)
        elif opcion == '3':
            numero = solicitar_numero()
            m = int(input("Ingrese el número de línea (1-10): "))
            mostrar_linea_tabla(numero, m)
        elif opcion == '4':
            print("¡Gracias por usar el programa! Hasta luego.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
menu()
