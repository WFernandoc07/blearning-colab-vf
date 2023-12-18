# 3. Fibonacci: Crea una lgoritmo para calcular el enésimo número de la secuencia de Fibonacci, donde F(0) = 0, F(1) = 1, y F(n) = F(n-1) + F(n-2) para n >= 2

n = int(input('Digite n: '))

aux = [0, 1]
j = 2

for i in range(n):
  aux.append(aux[j-1]+aux[j-2])
  j=j+1
  print(aux[i])

print('El término "n" de la serie Fibonacci es: ', aux[i])
