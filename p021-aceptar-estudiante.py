#aceptar estudiantes en base a ciertos criterios:
#nombre, edad y dos calificaciones; estudiantes +18
#calificaciones > 8

import os; os.system('cls')

print('Universidad One Piece')

nombre = input('Ingresa tu nombre, por favor: ')
edad = int(input('Introduce tu edad, por favor: '))

if edad < 18:
    print('Lo sentimos, solo aceptamos mayores de 18 años.')
else:
    print('Dame dos de tus calificaciones separadas por un espacio, por favor: ')
    c1, c2 = input().split()
    c1, c2 = int(c1), int(c2)

    if c1 < 8 or c2 < 8:
        print('Lo sentimos, solo aceptamos alumnos con calificaciones mayores a 8.')
    else:
        print(f'{nombre}, bienvenido(a) a la Universidad One Piece. Tu edad de {edad} años y tus calificaciones {c1},{c2} te lo permiten.')
