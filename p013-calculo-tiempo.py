#Calcular el equivalente de horas a dias, minutos y segundos

import os; os.system('cls')

print('Dada la hora, calcular su equivalente en días, minutos y segundos.')

hrs = int(input('¿Qué cantidad de horas quieres convertir? '))

dias = hrs / 24
mnt = hrs * 60
seg = hrs * 3600

#Sin comas para mostrarlos desde una sola línea y con el salto de línea
print(f'La(s) {hrs} horas equivalen a:\n {dias} dias\n {mnt} minutos\n {seg} segundos')