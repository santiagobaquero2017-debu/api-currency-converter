import requests

def consultar_cambio(moneda_origen, moneda_destino, monto):
    respuesta = requests.get(f"https://open.er-api.com/v6/latest/{moneda_origen}")
    datos = respuesta.json()
    
    tasa = datos["rates"][moneda_destino]
    resultado = monto * tasa
    
    print(f"\n{monto} {moneda_origen} = {resultado:.2f} {moneda_destino}")
    print(f"Tasa: {tasa}")
    print(f"Actualizado: {datos['time_last_update_utc']}")

# Prueba con diferentes monedas
consultar_cambio("USD", "COP", 1000)
consultar_cambio("USD", "BRL", 500)
consultar_cambio("EUR", "COP", 200)