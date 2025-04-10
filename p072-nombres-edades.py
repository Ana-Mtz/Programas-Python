## El usuario introduce nombres y edades, imprimir mayores de edad y el de mayor edad

import os;os.system('cls')

nom = []
edades = []

print('El usuario introduce nombres y edades, imprimir mayores de edad y el de mayor edad')

while True:
    nombre = input('Nombre: ')
    if not nombre=='':
        nom.append(nombre)
        edad = int(input('Edad: '))
        edades.append(edad)
    else:
        break

print(f'Nombres: {nom}')
print(f'Edades: {edades}')

print('\nLos mayores de edad son: ')
for i in range(len(edades)):
    if edades[i] >= 18:
        print(f'{nom[i]} - {edades[i]}')

print('\nEl de mayor edad es: ')
me = max(edades)
pos = edades.index(me)
print(f'{nom[pos]} - {edades[pos]}')