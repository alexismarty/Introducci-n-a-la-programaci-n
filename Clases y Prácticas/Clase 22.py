import requests

URL = "http://pad19.com:3030/adimra21" 

datos = {"apellido":"Perez", "nombre": "Juan"}

solicitud = requests.post(URL, data=datos)

print(solicitud.json())