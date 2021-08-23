#from math import perm
import math
from itertools import permutations, combinations

#FUNCIONES
def calcularPermutaciones(lista):
    totalPermutaciones = math.perm(len(lista))
    permutaciones = permutations(lista)

    print ("Total", totalPermutaciones)
    for item in permutaciones: print (item)

def calcularCombinaciones(lista, tomados):
    totalCombinaciones = 0
    combinaciones = combinations(lista, tomados)

    for item in combinations: 
        totalCombinaciones += 1
        print (item)
    print ("Total:", totalCombinaciones)

def main():
    lista = (1, 2, 3, 4)
    calcularPermutaciones(lista)
    calcularCombinaciones (lista,2)
    