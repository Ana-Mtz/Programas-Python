#Calcular el numero de la suerte en base al año de nacimiento

import os; os.system('cls')

print('Calcular el numero de la suerte en base al año de nacimiento.')

edad = int(input('Por favor, introduce tu año de nacimiento: '))

uni = edad % 10
edad = edad // 10
dec = edad % 10
edad = edad // 10
cen = edad % 10
edad = edad // 10
mill = edad % 10

numSuer = mill + cen + dec + uni

print(f'Los digitos individuales son: {mill}, {cen}, {dec}, {uni}')
print(f'Tu numero de la suerte es: {numSuer}')