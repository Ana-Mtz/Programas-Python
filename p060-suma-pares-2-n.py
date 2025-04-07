## Imprimir los pares de 2 a n y su suma

import os; os.system('cls')

print('Imprimir los pares de 2 a n y su suma :D')

n = int(input('Ingresa, por favor, hasta qué numero quieres llegar: '))
sum = 0

for i in range(2, n + 1, 2):
    print(i)
    sum += i
print(f'La suma de los numeros es: {sum}')
