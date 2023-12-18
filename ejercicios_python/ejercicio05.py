'''
4. Ordenamiento de Arreglos: Implementa algoritmos de ordenamiento,
como el Ordenamiento de Burbuja o el Ordenamiento por Inserción, para ordenar
una lista de números.
'''
print('Hello world')
numeros = [5, 8, 4, 12, 3, 17, 11, 19, 32, 34, 23, 1]
aux = 0

# Imprimir una lista
def imprimirLista(numeros):
    for i in range(len(numeros)):
        print(numeros[i])

# Ordenamiento por burbuja (bubble sort).
def ordenamientoBurbuja(numeros):
    for i in range(len(numeros)-1):
        for j in range(len(numeros)-1):
            if numeros[j]>numeros[j+1]:
                aux = numeros[j]
                numeros[j] = numeros[j+1]
                numeros[j+1] = aux

# Ordenamiento por inserción (insertion sort).
def ordenamientoInsercion(numeros):
    for i in range(len(numeros)-1):
        for j in range(len(numeros)-1):
            if numeros[j+1] < numeros[j]:
                aux = numeros[j+1]
                numeros[j+1] = numeros[j]
                numeros[j] = aux

print('---------- Ordenamiento Burbuja: --------')
ordenamientoBurbuja(numeros)
imprimirLista(numeros)
print('---------- Ordenamiento inserción: --------')
ordenamientoInsercion(numeros)
imprimirLista(numeros)
