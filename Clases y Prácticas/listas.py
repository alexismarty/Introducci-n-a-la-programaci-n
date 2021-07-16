mtrDatos = []

archivoDatos = open("datos.txt", "r")
#r significa que la acción es leer y si pongo w es escribir

mtrDatos = archivoDatos.read().split(",")
#split nos permite tomar ese archivo y convertirlo en una matriz. Uso la coma porque los elementos originales están searados por coma
# si estaría uno abajo del otro los separo con \n
archivoDatos.close()

print (mtrDatos)

for índice, ítem in enumerate(mtrDatos):
    mtrDatos[índice] = int(ítem)
    # Lo toma a cada elemento como un número y no como un caracter si uso el int

print (mtrDatos)