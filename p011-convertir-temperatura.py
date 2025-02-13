#Convertir los grados celcius a grados farenheit
import os; os.system('cls')

print('Calcular los grados farenheit dada una temperatura en grados celcius.')

celcius = float(input('Dame por favor los grados celcius a convertir: '))

far = ((celcius * (9 / 5)) + 32)

print(f'Los grados celcius dados equivalen a: {far} farenheit')