## Numeros del 1 al x usando el ciclo for

import os; os.system('cls')

x = int(input('¿Hasta donde quieres imprimir los numeros?: '))
i = int(input('¿En incremento de cuanto?: '))

for n in range(0, x + 1, i):
    print(n, end=' ')

print('\nLlegamos al final :D')