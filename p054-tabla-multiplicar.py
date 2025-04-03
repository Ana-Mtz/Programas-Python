## Imprimir la tabla de multiplicar con for

import os

while(True):
    os.system('cls')

    tab = int(input('¿Que tabla quieres imprimir?: '))
    n = int(input('¿Hasta donde quieres imprimirla?'))

    for i in range(1, n + 1):
        print(f'{tab} x {i} = {tab * i}')

    if input('\n¿Quieres imprimir otra tabla? (S/N): ').upper()=='N': break

print('\nProceso finalizado c:')