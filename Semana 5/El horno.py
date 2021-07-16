import random

## Límites a considerar
MAX_TEMPERATURA = 200
MIN_TEMPERATURA = 100

while (True):
    ## Punto 1
    print ()
    print ("CONTROL TEMPERATURA HORNO")
    print ()
    temperaturaAleatoria = random.randint(MIN_TEMPERATURA , MAX_TEMPERATURA)
    print ("Temperatura Objetivo:" , temperaturaAleatoria)
    print ()

    ## Punto 2
    temperaturaPrueba = int (input ("Ingresar temperartura entre 100°C y 200°C: "))
    if (temperaturaPrueba > 100 and temperaturaPrueba < 200):
        print ()

        ## Punto 3
        n1 = random.randint (temperaturaAleatoria - 2 , temperaturaAleatoria + 2)
        n2 = random.randint (temperaturaAleatoria - 2 , temperaturaAleatoria + 2)
        n3 = random.randint (temperaturaAleatoria - 2 , temperaturaAleatoria + 2)
        n4 = random.randint (temperaturaAleatoria - 2 , temperaturaAleatoria + 2)
        n5 = random.randint (temperaturaAleatoria - 2 , temperaturaAleatoria + 2)
        n6 = random.randint (temperaturaAleatoria - 2 , temperaturaAleatoria + 2)
        n7 = random.randint (temperaturaAleatoria - 2 , temperaturaAleatoria + 2)
        n8 = random.randint (temperaturaAleatoria - 2 , temperaturaAleatoria + 2)
        n9 = random.randint (temperaturaAleatoria - 2 , temperaturaAleatoria + 2)
        n10 = random.randint (temperaturaAleatoria - 2 , temperaturaAleatoria + 2)
        print ("Lectura aleatoria 1:" , n1)
        print ("Lectura aleatoria 2:" , n2)
        print ("Lectura aleatoria 3:" , n3)
        print ("Lectura aleatoria 4:" , n4)
        print ("Lectura aleatoria 5:" , n5)
        print ("Lectura aleatoria 6:" , n6)
        print ("Lectura aleatoria 7:" , n7)
        print ("Lectura aleatoria 8:" , n8)
        print ("Lectura aleatoria 9:" , n9)
        print ("Lectura aleatoria 10:" , n10)

        ## Punto 4
        promedioLecturas = (n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10) / 10
        print ()
        print ("PROMEDIO LECTURAS ALEATORIAS:" , promedioLecturas)
        print ()

        ## Punto 5
        if (promedioLecturas < temperaturaPrueba -2):
            print ("TEMPERATURA BAJA, se enciende el quemador")
        elif (promedioLecturas > temperaturaPrueba +2):
            print ("TEMPERATURA ALTA, se apaga el quemador")
        else:
            print ("HORNO ESTABLE")
    elif (temperaturaPrueba == 0):
            break
    else: 
        print ("TEMPERATURA INCORRECTA, ingresar temperatura entre 100°C y 200°C")
