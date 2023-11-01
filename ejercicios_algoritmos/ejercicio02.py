#Dadas 3 longitudes, diga si pueden formar un triángulo.
def determinaLogitudValida(longitud):
    if longitud > 0:
        return True
    else:
        return False
def digitarUnaLongitud(i):
    longitud = float(input(f'Digite una longitud {i}: '))
    return longitud

l1=0
l2=0
l3=0

while(l3<=0):
    if l1<=0:
        l1 = digitarUnaLongitud(1)
    else:
        if l2<=0:
            l2 = digitarUnaLongitud(2)
        else:
            l3 = digitarUnaLongitud(3)

print(f'l1: {l1}\nl2: {l2}\nl3: {l3}')

def determinarSiEsTriangulo(l1, l2, l3):
    if l1 + l2 > l3:
        if l2 + l3 > l1:
            if l3 + l1 > l2:
                return True
            else:
                return False
        return False
    return False

print(f'¿Es Triángulo?: {determinarSiEsTriangulo(l1,l2,l3)}')

