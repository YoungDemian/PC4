def contar_lineas_codigo(archivo_ruta):
    try:
        if not archivo_ruta.endswith('.py'):
            print("El archivo no tiene la extensión .py.")
            return
        with open(archivo_ruta, 'r') as archivo:
            lineas = archivo.readlines()
        lineas_codigo = 0
        for linea in lineas:
            linea_limpia = linea.strip()
            if linea_limpia and not linea_limpia.startswith('#'):
                lineas_codigo += 1
        print(f"El archivo tiene {lineas_codigo} líneas de código.")
    
    except FileNotFoundError:
        print("Archivo no encontrado. Por favor, ingresa una ruta válida.")
ruta_archivo = input("Introduce la ruta del archivo .py: ")
contar_lineas_codigo(ruta_archivo)
