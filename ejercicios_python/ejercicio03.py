'''Factorial: Escribe un algoritmo que calcule el factorial de un número entero n, denotado como n!.'''
n = int(input('Digite n: '))
prod_aux = 1

for i in range(n):
    prod_aux *= i+1

print('El factorial de ', n, 'es: ', prod_aux)
