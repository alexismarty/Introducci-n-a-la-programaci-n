import requests

#RUTA_ARCHIVO_REMOTO = "https://ssl.smn.gob.ar/dpd/observaciones/estadisticas.txt"
RUTA_ARCHIVO_REMOTO = "https://api.openweathermap.org/data/2.5/find?q=rafaela&mode=json&units=metric&lang=sp&appid=bbbe84df6ab458740a22a2e0a1eb7663"

contenidoRemoto = requests.get(RUTA_ARCHIVO_REMOTO)
#print (contenidoRemoto.status_code) #me sirve para ver si lo recibo bien, si es 200. Si es 404 no lo encontró y 500 un error interno
contenidoRemotoJson = contenidoRemoto.json()
print(contenidoRemotoJson)
print(contenidoRemotoJson["message"])
print(contenidoRemotoJson["cod"])
print(contenidoRemotoJson["count"])
print(contenidoRemotoJson["list"])
