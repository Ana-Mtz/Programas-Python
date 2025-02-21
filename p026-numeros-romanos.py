#Dado un numero entero entre 1 y 10, mostrar el equivalente en romano

import os; os.system('cls')

print('Dado un numero entre 1 y 10, mostrarlo en numero romano :D')

num = int(input('Por favor, ingresa el numero que quieras convertir a numero romano: '))

if num == 1:
    num_rom = 'I'
elif num == 2:
    num_rom = 'II'
elif num == 3:
    num_rom = 'III'
elif num == 4:
    num_rom ='IV'
elif num == 5:
    num_rom = 'V'
elif num == 6:
    num_rom = 'VI'
elif num == 7:
    num_rom = 'VII'
elif num == 8:
    num_rom = 'VIII'
elif num == 9:
    num_rom = 'IX'
elif num == 10:
    num_rom = 'X'
else:
    num('Numero invalido, por favor intenta nuevamente')

print(f'El numero {num} equivale a {num_rom} en numero romano')