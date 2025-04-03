## Imprimir multiplos de m entre 1 y n

import os 

while(True):
    os.system('cls')

    print('Imprimir multiplos de m entre 1 y n')
    n = int(input('¿Hasta donde quieres imprimir?: '))
    m = int(input('¿En multiplos de cuanto?: '))

    cn = sn = 0

    for i in range(1, n + 1):
        if i % m == 0:
            print(i, end=' ')
            sn += i
            cn += 1

    print(f'\nFueron {cn} multiplos, los cuales suman {sn}')

    if input('¿Deseas continuar? (S/N): ').upper()=='N': break

print('\nLlegamos al final :D')