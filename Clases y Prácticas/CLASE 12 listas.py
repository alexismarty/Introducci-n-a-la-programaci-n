mtrDatos = []

archivoDatos = open("datos.txt", "r")
mtrDatos = archivoDatos.read().split(",")
archivoDatos.close()

print(mtrDatos)

for indice, item in enumerate(mtrDatos):
    mtrDatos[indice] = int(item)

print(mtrDatos)
