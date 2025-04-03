## Numeros del x al 0 usando el ciclo for

import os; os.system('cls')

x = int(input('¿Desde donde quieres imprimir los numeros?: '))
i = int(input('¿En decremento de cuanto?: '))

for n in range(x, 0, -i):
    print(n, end=' ')

print('\nLlegamos al final :D')