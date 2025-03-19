#Imprime numeros del 1 al n

import os; os.system('cls')

n = int(input('¿Hasta qué numero?: '))
d = int(input('¿En incrementos de?'))
c = 0

while c <= n:
    print(c, end='')
    c += d
else:
    print('\n\n Valor final de c', c)

print('\nProceso terminado')