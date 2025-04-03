## Dado un numero entero como base y uno como exponente, calcular la base elevada al exponente

import os; os.system('cls')

base = int(input('Por favor, ingresa el valor de la base: '))
exp = int(input('Por favor, ingresa el valor del exponente: '))

r = 1

for _ in range(exp):
    r = r * base

print(f'{base} ^ {exp} = {r}')