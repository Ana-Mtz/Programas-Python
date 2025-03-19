#Imprime numeros del 1 al n

import os; os.system('cls')

n = int(input('¿Hasta qué numero?: '))
c = 1

while c <= n:
    print(c, end='')
    c += 1
else:
    print('\n\n Valor final de c', c)

print('\nProceso terminado')