#LIBRERIAS
import requests
import random
import pandas as pd

#DEFINICIONES
URL_API_CLIMA ="https://api.openweathermap.org/data/2.5/find?q=rafaela&mode=json&units=metric&lang=sp&APPID=bbbe84df6ab458740a22a2e0a1eb7663"

#FUNCIONES
def recuperarUrl(destino, formato):
    ##pass 
    ## pass lo uso cuando no tengo que definir algo en la función, como para completarlo momentaneamente
    consulta = requests.get(destino)

    if (consulta.status_code == 200):
        ## pass
        if (formato == "original"):
            return consulta.content
        elif (formato == "texto"):
            return consulta.txt
        elif (formato == "json"):
            return consulta.json()
        else:
            return False

    else:
        return False

def main():
    infoClima = recuperarUrl (URL_API_CLIMA, "json")
    temperatura = f'{infoClima ["list"][0]["main"]["temp"]:.1f}' 
    humedad = ["list"][0]["main"]["humidity"]
    presion = ["list"][0]["main"]["pressure"]
    print ("Temperatura: {temperatura} C")
    print ("Humedad: {humedad} %")
    print ("Presión: {temperatura} hPa")

#PRINCIPAL
if  __name__  ==  '__main__' :
	main ()
    