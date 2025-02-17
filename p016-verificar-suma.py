#Verificar si la suma de dos numeros enteros es igual a un tercero

import os; os.system('cls')

print('Verificar su la suma de dos numeros enteros es igual a un tercero')

print('Dame 3 numeros enteros separados por un <Enter>: ')
n1, n2, n3 = int(input()), int(input()), int(input())

if n1+n2 == n3:
    print('La suma de los dos primeros numeros es igual al tercero \n')
else:
    print('La suma de los dos primeros numeros NO es igual al tercero \n')

print('\n Gracias por utilizar este programa')
