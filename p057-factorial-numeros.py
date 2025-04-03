## Calcular el factorial de n numeros enteros

import os; os.system('cls')

print('Calcular el factorial de m numeros enteros')

num = int(input('Introduce hasta que numero deseas el factorial: '))

for x in range(1, num + 1):

    f = 1
    sec = ""

    for i in range(1, x + 1):
        f = f * i
        sec = sec + str(i)
        if i < x:
            sec = sec + " * "

    print(f'{x}! = {sec} = {f:,}')