#Dados tres numeros enteros, verificar cual es el mayor

import os; os.system('cls')

print('Verificar cual de los tres numeros es el mayor :)')

print('Ingresa, por favor, tres numeros enteros separados por un espacio: ')
n1, n2, n3 = input().split()
n1, n2, n3 = int(n1), int(n2), int(n3)

#comparamos primero n1
if n1 > n2 and n1 > n3:
    num_may = n1
#luego comparamos n2
elif n2 > n1 and n2 > n3:
    num_may = n2
#y por ultimo n3
else:
    num_may = n3

print(f'El numero mayor es: {num_may}')