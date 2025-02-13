#Calcular el volumen de un cilindro dado su radio y su altura

import math as m
import os; os.system('cls')

print('Calcular el volumen de un cilindro dado el radio y la altura.')

print('Por favor, ingresa el radio y la altura, separados por un espacio:')
r, h = input().split()
r, h = float(r), float(h)

v = m.pi * pow(r, 2) * h

print(f'El volumen del cilindro es: {v}')