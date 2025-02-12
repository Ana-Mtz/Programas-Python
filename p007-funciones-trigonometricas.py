#Ejemplifica el uso de funciones trigonométricas del modulo math

import math as m
import os; os.system('cls')

print('Calculo de las funciones trigonométricas básicas')
angulo =float(input('Dame un ángulo en radianes: '))#va de adentro hacia afuera

seno = m.sin(angulo)
coseno = m.cos(angulo)
tangente = m.tan(angulo)

grados = m.degrees(angulo)

salida = (
    'Resumen de funciones \n'
    f'El seno es: {seno} \n'
    f'El coseno es: {coseno} \n'
    f'La tangente es: {tangente} \n'
    f'El angulo {angulo} en radianes equivale a: {grados} grados \n'
)

print(salida)