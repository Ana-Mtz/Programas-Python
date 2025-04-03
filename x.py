## Calcular el factorial de n numeros enteros

import os; os.system('cls')

print('Calcula e imprime el factorial de todos los numeros desde 1 hasta el que el usuario decida')

num = int(input('Dame un numero entero: '))

for x in range(1, num + 1):

    f = 1
    sec = ""

    for i in range(1, x + 1):
        f *= i
        sec += str(i)
        if i < x:
            sec += " * "

    print(f'{x}! = {sec} = {f:,}')