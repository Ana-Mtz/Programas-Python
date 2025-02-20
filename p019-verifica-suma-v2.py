#Dados tres números enteros positivos, verificar si la suma de dos de ellos es igual 
#a alguno de los otros

import os; os.system('cls')

print('Verificar su la suma de dos numeros es igual a un tercero')

print('Por favor, dame 3 numeros enteros separados por un espacio: ')
n1, n2, n3 = input().split()
n1, n2, n3 = int(n1), int(n2), int(n3)

if n1 + n2 == n3:
    print(f'{n1} + {n2} = {n3}')
elif n1 + n3 == n2:
    print(f'{n1} + {n3} = {n2}')
elif n2 + n3 == n1:
    print(f'{n2} + {n3} = {n1}')
else:
    print('Posiblemente son iguales')