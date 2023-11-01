#Leer una cantidad sol expresada en soles. Si es sol< 0 Escribir “Valor incorrecto”.
#En caso contrario, si sol < 100 transformarla a su equivalente en dólares,
#sino expresarla en Euros. (Considerar 1 $ = 3.25 soles, 1 Euro = 4.20 soles).
sol = int(input('Digite una cantidad: '))

def convertirMoneda(sol):
    if sol < 0:
        return 'Valor incorrecto'
    else:
        if sol < 100:
            sol = 3.25*sol
            return f'{sol} dólares'
        else:
            sol = 4.20*sol
            return f'{sol} euros'

print(convertirMoneda(sol))
