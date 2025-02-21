#Calcular el promedio de 5 calificaciones y mandar un mensaje posteriormente

import os; os.system('cls')

print('Dadas 5 calificaciones, obtener el promedio y mostrar un mensaje en pantalla :3 ')

print('Por favor, introduce las cinco calificaciones separadas por un espacio: ')
c1, c2, c3, c4, c5 = input().split()
#decidí manejar enteros, en lugar de flotantes :3
c1, c2, c3, c4, c5 = int(c1), int(c2), int(c3), int(c4), int(c5)

prom = (c1 + c2 + c3 + c4 + c5)/5

print(f'Tu promedio es: {prom}')

if prom >= 0 and prom < 6:
    print('Estas reprobado :( )')
elif prom >= 6 and prom < 7:
    print('Pasaste de panzazo :| ')
elif prom >= 7 and prom < 8:
    print('Muy bien, aunque puedes mejorar :) ')
elif prom >= 8 and prom < 9:
    print('Excelente, sigue así :D ')
elif prom >= 9 and prom <= 10:
    print('¡Felicidades! Tu esfuerzo valió la pena :3 ')
else:
    print('Respuesta invalida, por favor ingresa los datos nuevamente')