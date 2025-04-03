## Suma de n numeros introducidos por el usuario usando ciclo for

import os

while(True):
    os.system('cls')

    cuantos = int(input('¿Cuantas calificaciones deseas procesar?: '))
    sum = 0
    cadnum = ''

    for i in range(1, cuantos + 1):
        n = int(input(f'Calificacion [{i}] = '))
        sum += n
        cadnum = cadnum + ',' + str(n)

    print(f'Los numeros que introdujiste fueron: {cadnum}')
    print(f'La suma es {sum}, el promedio es {sum/n}')

    if input('\n¿Deseas continuar? (S/N): ').upper()=='N': break

print('\nLlegamos al final :D')