# LIBRERIAS
import requests

# DEFINICIONES
RUTA_ARCHIVO_REMOTO = "https://ssl.smn.gob.ar/dpd/observaciones/estadisticas.txt"
URL_API_CLIMA = "https://api.openweathermap.org/data/2.5/find?q=rafaela&mode=json&units=metric&lang=sp&appid=bbbe84df6ab458740a22a2e0a1eb7663"

# FUNCIONES 
def recuperarUrl(destino, formato):
    #pass
    consulta = requests.get(destino, formato)
    if (consulta.status_code == 200):
        if (formato == "original"):
            return consulta.content # Me devuelve el formato tal cual me da el servidor
        elif (formato == "texto"):
            return consulta.text #Me devuelve en formato en texto
        elif (formato == "json"):
            return consulta.json() #Me devuelve en formato en json
        else:
            return False
    else:
        return False
    


def main():
    # infoClima = recuperarUrl(URL_API_CLIMA, "original")
    # print (infoClima)
    # infoClima1 = recuperarUrl(URL_API_CLIMA, "texto")
    # print (infoClima1)
    infoClima2 = recuperarUrl(URL_API_CLIMA, "json")
    temperatura = f'{infoClima2 ["list"][0]["main"]["temp"]:.2f}'
    print (temperatura)
    # infoClima3 = recuperarUrl(URL_API_CLIMA, "normal")
    # print (infoClima3)
    # infoClima4 = recuperarUrl(RUTA_ARCHIVO_REMOTO, "texto")
    # print (infoClima4)

# PRINCIPAL
if (__name__ == "__main__"):
    main()