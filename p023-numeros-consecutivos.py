#Verificar si los numeros dados son consecutivos o no

import os; os.system('cls')

print('Dados 3 numeros enteros verificar si son consecutivos :D')

print('Por favor, ingresa tres numeros enteros consecutivos separados por un espacio: ')
n1, n2, n3 = input().split()
n1, n2, n3 = int(n1), int(n2), int(n3)

if n2 == n1 + 1 and n3 == n2 + 1:
    print(f'Los numeros {n1}, {n2} y {n3} son consecutivos.')
else:
    print('Los numeros no son consecutivos, intentalo de nuevo.')