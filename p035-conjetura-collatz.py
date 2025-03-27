## Calcula la conjetura de collatz

import os 

while(True):
    os.system('cls')
    print('Imprime la conjetura de Collatz \n')

    n = int(input('Introduce un numero entero positivo, por favor: '))
    c = 0

    while n != 1:
        print(n, end=' ')
        c += 1
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    print(n, end=' ')
    print('\nPasos: ', c)

    if input('¿Deseas continuar? (S/N): ').upper()=='N': break

print('\nProceso finalizado :) \n')