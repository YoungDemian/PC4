import csv
import os
input_file = 'temperaturas.txt'
output_file = 'resumen_temperaturas.txt'
if not os.path.exists(input_file):
    print(f"El archivo {input_file} no se encuentra en el directorio.")
else:
    temperaturas = []
    with open(input_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) == 2:
                fecha, temperatura = row
                try:
                    temperaturas.append(float(temperatura))
                except ValueError:
                    print(f"Valor no válido en la línea: {row}")

    if temperaturas:
        temp_promedio = sum(temperaturas) / len(temperaturas)
        temp_maxima = max(temperaturas)
        temp_minima = min(temperaturas)

        with open(output_file, 'w') as f_out:
            f_out.write(f'Temperatura promedio: {temp_promedio:.2f}°C\n')
            f_out.write(f'Temperatura máxima: {temp_maxima:.2f}°C\n')
            f_out.write(f'Temperatura mínima: {temp_minima:.2f}°C\n')

        print("Resumen de temperaturas guardado en 'resumen_temperaturas.txt'.")
    else:
        print("No se encontraron temperaturas válidas en el archivo.")
        
