#Dado el nombre, sexo, edad y 3 calificaciones del estudiante decidir si es aceptado
#condiciones adicionales:
#la universidad es solo para mujeres mayores de 21 años con promedio de entre 8 y 9.5

import os; os.system('cls')

print('Dadas ciertas características, decidir si el aspirante es aceptado o no :P \n')

print('Bienvenido a la Universidad de Kitty Kat')

nom = input('Por favor, introduce tu nombre: ')
sexo = input('Por favor, introduce tu sexo (h/m): ')
edad = int(input('Por favor, introduce tu edad: '))
print('Por favor, introduce tres calificaciones, separadas por un espacio: ')
c1, c2, c3 = input().split()
c1, c2, c3 = int(c1), int(c2), int(c3)
prom = (c1 + c2 + c3)/3

#aceptada
if sexo == 'm' and edad > 21 and prom >= 8 and prom <= 9.5:
    print(f'{nom} has sido aceptada. Tu edad de {edad} años y tu promedio de {prom} lo permiten')
#no aceptada x h
elif sexo == 'h': #and edad > 21 and prom >= 8 and prom <= 9.5:
    print(f'{nom} has sido rechazado. Solo aceptamos mujeres')
#no aceptada x edad
elif edad < 21:
    print(f'{nom}, eres mujer pero no tienes la edad suficiente')
#no aceptada x promedio
else:
    print('No cumples con los requisitos.')
