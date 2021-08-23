#LIBRERÍAS
import os
from dotenv import load_dotenv
import requests as req
import pandas as pd
load_dotenv()



#DEFINICIONES 
SERVIDOR = os.getenv("SERVIDOR_PRODUCTOS")
ENDPOINT_PEDIDOS = os.getenv("ENDPOINT_PEDIDOS")
ENDPOINT_PRODUCTOS = os.getenv("ENDPOINT_PRODUCTOS")
ENDPOINT_CONSULTA_PEDIDOS = os.getenv("ENDPOINT_CONSULTA_PEDIDOS")
TOKEN = os.getenv ("TOKEN_PRODUCTOS")
URL_TELEGRAM = os.getenv ("URL_TELEGRAM")
TOKEN_TELEGRAM = os.getenv ("TOKEN_TELEGRAM")
ENDPOINT_TELEGRAM = os.getenv ("ENDPOINT_TELEGRAM")
ID_CHAT = os.getenv ("ID_CHAT")
URL_CONSULTA_PRODUCTO = f"{SERVIDOR}/{ENDPOINT_PRODUCTOS}?token={TOKEN}"
URL_PEDIDO = f"{SERVIDOR}/{ENDPOINT_PEDIDOS}?token={TOKEN}"
URL_CONSULTA_PRODUCTOS = f"{SERVIDOR}/{ENDPOINT_PRODUCTOS}?token={TOKEN}"
SEPARADOR_POR_FUNCIONES = "******************************************************************************"
SEPARADOR_INTERNO = "------------------------------------------------------------------------------"



# FUNCIONES
def consultarProductos(destino):
    print (SEPARADOR_POR_FUNCIONES)
    print ("CONSULTA DE LISTA DE PRODUCTOS")
    print ()
    consultaListaProductos = req.get(URL_CONSULTA_PRODUCTO)
    if (consultaListaProductos.status_code == 200):
        print ("CONEXIÓN EXITOSA. A continuación se muestra la lista")
        print ()
        resultadoConsulta = consultaListaProductos.json()
        for productos in resultadoConsulta ['productos']:
            print (SEPARADOR_INTERNO)
            print ("Id:",productos['id'])
            print ("Nombre:",productos['nombre'])
            print ("Precio:",productos['precio'])
            print ("Stock:",productos['stock'])
        # print (resultadoConsulta)
    else:
        print ("ERROR DE CONEXIÓN")

def cargarPedidos(destino):
    while (True):
        print()
        print (SEPARADOR_POR_FUNCIONES)
        print ("CARGA DE PEDIDO")
        print ("Presione # para finalizar la carga")
        idProducto = input ("INGRESE ID DEL PRODUCTO: ")
        if (idProducto == "#"):
            break
        cantidadProducto = input ("INGRESE CANTIDAD: ")
        if (cantidadProducto == "#"):
            break
        cadenaJson = {"id:":idProducto, "cantidad:":cantidadProducto}
        pedido = req.post (URL_PEDIDO, cadenaJson)
        if (pedido.status_code == 200):
            ordenPedido = pedido.json()
            print()
            print (SEPARADOR_INTERNO)
            print ("Confirmación:", ordenPedido['mensaje'])
            print ("Código del pedido:", ordenPedido['codigo'])
            print (SEPARADOR_INTERNO)
            #print (ordenPedido)
        else: 
            print ("ERROR. NO SE PUDO REALIZAR EL PEDIDO")
                    

def consultarPedidos ():
    while (True):
        print ()
        print (SEPARADOR_POR_FUNCIONES)
        print ("CONSULTA DEL PEDIDO")
        print ("Presione # para finalizar la consulta")
        idPedido = input ("INGRESE EL CÓDIGO DEL PEDIDO: ")
        URL_CONSULTA_PEDIDOS = f"{SERVIDOR}/{ENDPOINT_CONSULTA_PEDIDOS}{idPedido}?token={TOKEN}"
        if (idPedido == "#"):
            break
        consultaPedidos = req.get (URL_CONSULTA_PEDIDOS)
        if (consultaPedidos.status_code == 200):
            detallePedido = consultaPedidos.json()
            print()
            print (SEPARADOR_INTERNO)
            print ("DETALLES DEL PEDIDO")
            print ("Id del producto:", detallePedido['productos']['id:'])
            print ("Cantidad solicitada:", detallePedido['productos']['cantidad:'])
                        
        else:
            print ("ERROR. No se puede consultar")
        idProducto = int(detallePedido['productos']['id:'])
        cantidadProducto = int (detallePedido ['productos']['cantidad:'])
        consultaListaProductos = req.get(URL_CONSULTA_PRODUCTOS)
        resultado = consultaListaProductos.json()
        stock = resultado['productos'][idProducto-1]['stock']
        print ("El stock de este producto es:", stock)

        if (stock >= cantidadProducto):
            print ("EL PEDIDO SE PUEDE PROCESAR")
            ## NO PUDIMOS TRABAJAR FORMANDO LA URL CON LA FUNCIÓN MACRO ##
            #TEXTO = f"El pedido N°{idPedido} puede procesarse. Se pidieron {cantidadProducto} unidades del producto y en stock hay {stock} unidades."
            URL_MENSAJE_TELEGRAM= "https://api.telegram.org/bot1973714579:AAG3CP2ukyX2nYgToC5VCw-E5p7AXnF7Vvg/sendMessage?chat_id=-559723042&text=El pedido pudo procesarse correctamente."
            #URL_MENSAJE_TELEGRAM = f"{URL_TELEGRAM}{TOKEN_TELEGRAM}/{ENDPOINT_TELEGRAM}?chat_id={ID_CHAT}&text={TEXTO}"
            consulta = req.get(URL_MENSAJE_TELEGRAM)
            if (consulta.status_code == 200):
                print ("NOTIFICADO POR TELEGRAM")
            else: 
                print ("ERROR. NO SE PUEDE NOTIFICAR POR TELEGRAM")
        else:
            print ("El pedido no puede procesarse. La cantidad solicitada supera el stock.")
            #TEXTO1 = f"El pedido N°{idPedido} NO puede procesarse. Se pidieron {cantidadProducto} unidades del producto y en stock hay {stock} unidades."
            URL_MENSAJE = "https://api.telegram.org/bot1973714579:AAG3CP2ukyX2nYgToC5VCw-E5p7AXnF7Vvg/sendMessage?chat_id=-559723042&text=El pedido no pudo procesarse, el stock no es el suficiente."
            #URL_MENSAJE = f"{URL_TELEGRAM}{TOKEN_TELEGRAM}/{ENDPOINT_TELEGRAM}?chat_id={ID_CHAT}&text={TEXTO1}"
            consultaTelegram = req.get(URL_MENSAJE)	
            if (consultaTelegram.status_code == 200):	
                print ("NOTIFICADO POR TELEGRAM")
            else: 
                print ("ERROR. NO SE PUEDE NOTIFICAR POR TELEGRAM")
        print (SEPARADOR_INTERNO)

        


def main():
    datosConsultados = consultarProductos(URL_CONSULTA_PRODUCTO)
    print (datosConsultados)
    pedidosCargados = cargarPedidos(URL_PEDIDO)
    print (pedidosCargados)
    consultasPedidos = consultarPedidos()
    print (consultasPedidos)

#PRINCIPAL
if (__name__ == "__main__"): 
    main()
