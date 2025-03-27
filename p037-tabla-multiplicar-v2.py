## Imprime las tablas del 1 hasta n, hasta el 10

import os

while(True):
    os.system('cls')
    print('Imprimiendo las tablas de multiplicar')
    
    n = int(input('Hasta qué tabla quieres imprimir? '))
    m = int(input('Hasta donde se debe imprimir la tabla? '))
    t = 1

    while t <= n:
        print(f'\nTabla {t}\n')

        c = 1
        while c <= m:
            print(f'{t} x {c} = { t * c }')
            c += 1

        t+=1

    if input('¿Deseas continuar? (S/N): ').upper()=='N': break

print('\nProceso finalizado :) \n')