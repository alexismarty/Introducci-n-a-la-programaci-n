#def main ():
 #   print ("Función Principal")

#if (__name__ == "__main__"): #Si el script es llamado de forma directa
   # main()

## FORMAS DE ESCRIBIR UN PRINT
def main ():
    valor = 23.64
    signo = "$"
    mensaje1 = "El importe es de " + signo + " " + str (valor) + " " +"AR"  #si no le agregaría el str no me toma el valor porque es flotante
    mensaje2 = f"El importe es de {signo} {valor:.3f} AR" #placeholder #.3f me da tres decimales
    mensaje3 = "El importe es de {0} {1} AR".format (signo, valor)
    print (mensaje1)
    print (mensaje2)
    print (mensaje3)

if (__name__ == "__main__"): #Si el script es llamado de forma directa
    main()