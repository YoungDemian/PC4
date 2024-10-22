import requests
def obtener_precio_bitcoin():
    try:
        respuesta = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        respuesta.raise_for_status()
        datos = respuesta.json() 
        precio_usd = datos['bpi']['USD']['rate_float']
        return precio_usd
    except requests.RequestException as e:
        print("Error al obtener el precio de Bitcoin:", e)
        return None

# Función principal
def main():
    try:
        cantidad_bitcoins = float(input("Ingrese la cantidad de bitcoins que posee: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return
    precio_bitcoin_usd = obtener_precio_bitcoin()
    if precio_bitcoin_usd is not None:
        valor_total_usd = cantidad_bitcoins * precio_bitcoin_usd
        print(f"El valor de {cantidad_bitcoins} bitcoins es: ${valor_total_usd:,.4f} USD")

if __name__ == "__main__":
    main()
