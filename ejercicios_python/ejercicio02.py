# Suma de Números: Escribe un algoritmo que sume todoslos
#los números enteros desde 1 hasta un número dado n.

n = int(input('Digite n: '))
sum_aux = 0;
for i in range(n):
    sum_aux += i+1
print('La suma es: ', sum_aux)

    
