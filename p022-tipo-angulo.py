#Mostrar al tipo de angulo en base a:
#<90-agudo, =90-recto, >90 y >180- obtuso, =180-llano, >180 y <360-concavo

import os; os.system('cls')

print('Mostrando el tipo de angulo en base a los grados')

ang = int(input('Ingresa un angulo para clasificarlo: '))

print(f'El angulo tiene {ang} grados, por lo tanto es un angulo: ',end='')

if ang < 90:
    print('agudo')
elif ang == 90:
    print('recto')
elif ang > 90 and ang < 180:
    print('obtuso')
elif ang == 180:
    print('llano')
elif ang > 180 and ang <360:
    print('concavo')
else:
    print('El angulo esta fuera del rango.')