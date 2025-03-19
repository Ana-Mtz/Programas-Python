#Imprime numeros del 1 al n

import os; os.system('cls')

n = int(input('¿Hasta qué numero?: '))
d = int(input('¿En decremento de?: '))
c = n

while c >= 1:
    print(c, end=' ')
    c -= d
else:
    print('\n\nValor final de c', c)

print('\nProceso terminado')