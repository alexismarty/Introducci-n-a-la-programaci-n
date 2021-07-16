#LIBRERIAS
import requests
import time

#DEFINICIONES
URL_REMOTA = "https://api.covid19api.com/summary"


#FUNCIONES
def recuperarUrl(destino):
    consulta = requests.get(destino)
    if (consulta.status_code == 200):
        return consulta.json ()
    if (consulta.status_code == 404):
        print ("No se encuentra la página")
    else:
        return False



def main():
    ## Datos recuperados de la URL proporcionada
    datosRecuperados = recuperarUrl(URL_REMOTA)
    print ()
    print ("CONSULTA REMOTA A LA URL PROPORCIONADA:")
    print ("Datos obtenidos con éxito")
    print ()

    ## Recuperar la fecha de la última actualización
    cadenaFecha = datosRecuperados ["Global"]["Date"]
    cadenaFecha1 = cadenaFecha [0:19] 
    formato = "%Y-%m-%dT%H:%M:%S" 
    fecha = time.strptime(cadenaFecha1, formato)
    fechaConvertida = f'Fecha:{fecha.tm_mday}/{fecha.tm_mon}/{fecha.tm_year} y Hora:{fecha.tm_hour}:{fecha.tm_min}'
    print ()
    print ("ÚLTIMA ACTUALIZACIÓN DE LA PÁGINA")
    print(fechaConvertida)
    print ()

    ## Diccionario de datos argentinos
    datosArgentinos = datosRecuperados["Countries"][6]
    print ()
    print ("DATOS ARGENTINOS")
    print (datosArgentinos)
    print ()

    ## Copia de los datos argentinos en el directorio local
    archivo = open ("DATOS_ARGENTINOS.json","w")
    archivo.write(str(datosArgentinos))
    archivo.close()
    print ()
    print ("EL ARCHIVO: DATOS_ARGENTINOS.json FUE ALMACENADO LOCALMENTE")
    print ()

    ## Datos importantes para Argentina
    nuevosConfirmados = f'Nuevos confirmados: {datosArgentinos ["NewConfirmed"]}'
    totalConfirmados = datosArgentinos ["TotalConfirmed"]
    nuevasMuertes = f'Nuevas muertes: {datosArgentinos ["NewDeaths"]}'
    totalMuertes = f'Total muertes: {datosArgentinos ["TotalDeaths"]}'
    nuevosRecuperados = f'Nuevos recuperados: {datosArgentinos ["NewRecovered"]}'
    totalRecuperados = datosArgentinos ["TotalRecovered"]
    print ()
    print ("DATOS IMPORTANTES DE ARGENTINA")
    print (nuevosConfirmados)
    print ("Total confirmados:", totalConfirmados)
    print (nuevasMuertes)
    print (nuevosRecuperados)
    print ("Total recuperados:", totalRecuperados)
    print ()

    ## Porcentajes
    confirmadosGlobal = datosRecuperados ["Global"]["TotalConfirmed"]
    porcentajeConfirmadosAr = f'Porcentaje Total Confirmados: {totalConfirmados*100/confirmadosGlobal:.2f}%'
    recuperadosGlobal = datosRecuperados ["Global"]["TotalRecovered"]
    porcentajeRecuperadosAr = f'Porcentaje Total Recuperados: {totalRecuperados*100/recuperadosGlobal:.2f}'
    print ()
    print ("PORCENTAJES DE DATOS ARGENTINOS EN RELACIÓN A LO GLOBAL")
    print (porcentajeConfirmadosAr)
    print (porcentajeRecuperadosAr)
    print ()


# ACLARACIONES
    ## En el punto 1 solo pide solicitar por eso no imprimimos todos los datosRecuperados
    ## Tuvimos muchos inconvenientes con la última partecita del formato como que todoos los días cambiaba, 
    # por eso lo sacamos y tuvimos que recortar la fecha.
    ## En el punto 4, en totalConfirmados y totalRecuperados, no pudimos usar f porque después lo 
    # necesitabamos como entero para los %

#PRINCIPAL
if (__name__ == "__main__"): 
    main()
