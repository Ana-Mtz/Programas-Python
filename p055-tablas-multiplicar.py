## Imprimir las tablas del 1 al 10 hasta el 10

import os; os.system('cls')

tab = int(input('Imprimir las tablas del 1 al...?: '))
n = int(input('¿Hasta donde quieres imprimir las tablas?: '))

for tab in range(1, n + 1):
    print(f'Tabla del {tab}: ')

    for i in range(1, n + 1):
        print(f'{tab} x {i} = {tab * i}')

    print()