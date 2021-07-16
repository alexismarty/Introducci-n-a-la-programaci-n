
import random

ctdPares = 0
ctdImpares = 0
ctdNúmeros = 0

# print ("Pares: ", ctdPares)

while(True): 
    ctdNúmeros = int (input("Ingresar cantidad de números para trabajar: "))
    if (ctdNúmeros > 0 and ctdNúmeros <= 20):
        break

for interacciones in range (ctdNúmeros): 
    nroAlAzar = random.randint(1,200)
    print (nroAlAzar)

    if (nroAlAzar % 2 == 0):
        ctdPares = ctdPares + 1
    else:
        ctdImpares = ctdImpares + 1

print ()
print ("Pares", ctdPares)
print ("Impares", ctdImpares)