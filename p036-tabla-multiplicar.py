## Imprime la tabla de multiplicar t, hasta n

import os

while (True):
    os.system('cls')
    print('Imprimiendo tabla de multiplicar\n')

    tab = int(input('Introduce la tabla que quieres imprimir: '))
    n = int(input('Hasta donde quieres imprimirlo?: '))
    k = 1

    while k <= n:
        print(f'{tab} x {k} = {tab * k}')
        k+=1
    if input('¿Deseas continuar? (S/N): ').upper()=='N': break

print('\nProceso finalizado c: \n')