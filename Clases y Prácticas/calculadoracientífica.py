import math


print ("1- Seno")
print ("2- Coseno")
print ("3- Tangente")
print ("4- Cuadrado")
print ("5- Raíz cuadrada")

while (True):
    print ()
    numeroAOperar = float (input("Igresar número: "))
    tipoOperacion = int (input ("Ingresar tipo operación "))

    if (tipoOperacion == 1):
        print (math.sin(numeroAOperar))
    elif (tipoOperacion == 2):
        print (math.cos(numeroAOperar))
    elif (tipoOperacion == 3):
        print (math.tan(numeroAOperar))
    elif (tipoOperacion == 4):
        print (numeroAOperar * numeroAOperar)
    elif (tipoOperacion == 5):
        print (math.sqrt(numeroAOperar))
    else:
        print ("Operación no válida")
    