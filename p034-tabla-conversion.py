## Tabla de conversion de Peso (MNX) a Dollar ($)

import os;

while(True):
    os.system('cls')
    print('Tabla de conversion de Peso(MNX) a Dolar ($) \n')

    tipCam = 20.50
    pi = float(input('Valor inicial: '))
    pf = float(input('Valor final: '))
    c = pi #c tiene el control del proceso
    print('\nPeso\tDolar')
    print('-'*15)

    while c <= pf: #estas ldc son las que imprimen la tabla
        print(f'{c}\t{c/tipCam:.2f}')
        c += 1
    print('-'*15)

    if input('¿Deseas continuar? (S/N): ').upper()=='N': break

print('\nProceso finalizado :) \n')