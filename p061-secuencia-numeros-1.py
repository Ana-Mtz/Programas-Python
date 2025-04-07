## Imprimir la secuencia de numeros mostrando el numero de renglones

import os; os.system('cls')

print('Imprimir la secuencia de numeros mostrando el numero de renglones :)')

n = int(input('Por favor, ingresa un numero: '))

for i in range(1, n + 1):
    for l in range(1, i + 1):
        print(i,end='')
    print()