# DEFINICIONES
# Simplemente por orden, declaramos algunas constantes y variables generales al inicio
# Recordar que Python no cuenta con un comando para declarar constantes, básicamente todos
# los elementos son considerados variables desde el momento en el cual se inicializan,
# por esa razón elegimos utilizar nomenclatura en MAYUSCULAS que nos permite ubicar fácilmente
# las constantes de manera visual.
AÑO = 365
SEMESTRE1 = 183
SEMESTRE2 = 182
INGRESO_ALTO = 8000

# Si no utilizamos la alternativa de retorno de valores múltiples en procesarCalculos,
# deberemos declarar algunas variables globales que nos comprometerán a guardar los cálculos generales.
ingresosTotales = 0
ingresosSemestre1 = 0
ingresosSemestre2 = 0
promedioSemestre1 = 0
promedioSemestre2 = 0
promedioGeneral = 0
diasAltoIngreso = 0
porcDiasAltoIngreso = 0



# FUNCIONES
# Declaramos las funciones a utilizar, recordar hacerlo previamente a su llamado.
def cargarDatosIntDesdeArchivo ():
    # Abrimos ruta para lectura.
    archivo = open("ingresos_diarios_2020.txt", "r")
    # Leemos el contenido, separándolo por comas y cargándolo en la lista lectura.
    lectura = archivo.read().split(",")
    archivo.close()

    for indice, item in enumerate (lectura):
        # Recorremos la lista para convertir cada elemento a entero mediante la función int ().
		# A esto se lo conoce normalmente con el término casting.
        lectura [indice] = int (item)
    # Finalmente la función "devuelve" la lista convertida
    return lectura

def procesarCalculos ():
    global ingresosSemestre1
    global ingresosSemestre2
    global promedioSemestre1
    global promedioSemestre2
    global promedioGeneral
    global diasAltoIngreso
    global porcDiasAltoIngreso
   
    # CÁLCULOS REQUERIDOS
    # Utilizamos un único for () para iterar listaIngresos y contabilizar 1er semestre,
	# 2do semestre y días de alto ingreso
    for indice, item in enumerate (listaIngresos):
        if (indice < SEMESTRE1):
            ingresosSemestre1 = ingresosSemestre1 + item
        else:
            ingresosSemestre2 = ingresosSemestre2 + item
        if (item >= INGRESO_ALTO):
            diasAltoIngreso = diasAltoIngreso + 1            
    promedioSemestre1 = int (ingresosSemestre1 / SEMESTRE1)
    promedioSemestre2 = int (ingresosSemestre2/SEMESTRE2)
    promedioGeneral = (promedioSemestre1 + promedioSemestre2)/2
    porcDiasAltoIngreso = int ((diasAltoIngreso/AÑO)*100)

    # Realizados los 4 cálculos, simplemente los retornamos como resultado de la función
	# Si no utilizáramos retorno de valor / es, deberíamos trabajar con variables globales,
	# indicando su uso mediante el comando global, como se puede ver en las primeras líneas
	# comentadas al principio de la función

def ordenarMayoraMenor():
    global mayorYMenor

    mayorYMenor = []
    paraElegir = open ("ingresos_diarios_2020.txt", "r")
    mayorYMenor = paraElegir.read().split(",")
    paraElegir.close
    mayorYMenor.sort(reverse = True)



# BLOQUE CENTRAL
# Llamamos a la función cargarDatosIntDesdeArchivo (), pasándole un argumento que
# es el nombre del archivo desde el cual debe recuperar los registros.
# La función nos "devolverá" una lista de enteros que asignaremos a lista
listaIngresos = cargarDatosIntDesdeArchivo ()


# EJEMPLO ALCANCE DE VARIABLE
procesarCalculos ()
ordenarMayoraMenor ()

# No sabíamos donde ponerlo, lo definimos como función pero no funcionaba hasta que usamos el global
# mayorYMenor = []
# paraElegir = open ("ingresos_diarios_2020.txt", "r")
# mayorYMenor = paraElegir.read().split(",")
# paraElegir.close
# mayorYMenor.sort(reverse = True)

#SALIDA DE INFORMACIÓN
# print ("Promedio diario Semestre 1:", promedioSemestre1)
# print ("Promedio diario Semestre 2:", promedioSemestre2)
print ()
print ("Promedios diarios semestres 1 y 2:  $ {0} AR y $ {1} AR".format (promedioSemestre1, promedioSemestre2) )
print()
print ("Promedio diario General: $ {0} AR".format(promedioGeneral))
print ()
print ("Porcentaje días con Alto Ingreso: {0} %".format(porcDiasAltoIngreso))
print ()
print ("Monto del día de mayor ingreso: $ {0} AR".format(mayorYMenor[0]))
print() 
print ("Monto del día de menor ingreso: $ {0} AR".format(mayorYMenor[364]))
print ()