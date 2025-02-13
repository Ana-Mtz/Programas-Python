#Calcular el tercer angulo, dados dos angulos

import os; os.system('cls')

print('Dados dos angulos, calcular el tercero.')

#siempre especificar el tipo de var y el input (para que el usuario introduzca los datos)
ang1 = int(input('Por favor, ingresa el primer angulo: '))

ang2 = int(input('Por favor, ingresa el segundo angulo: '))

ang3 = 180 - (ang1 + ang2)

print(f'El tercer angulo resultante es de: {ang3} grados')