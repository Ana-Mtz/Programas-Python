#segunda ley de newton f = m * a

import os; os.system('cls')

print('Calculando los valores de la segunda ley de Newton \n')
print('Calcular la fuerza ... [1]')
print('Calcular la masa ... [2]')
print('Calcular la aceleracion ... [3]')

op = int(input('\n ¿Qué opción elijes?: '))

if op == 1:
    print('\n Calculando la fuerza...')
    m = int(input('Dame el valor de la masa, por favor: '))
    a = int(input('Dame el valor de la aceleración, por favor: '))
    f = m * a
    print(f'El resultado de la fuerza es: {f}')
elif op == 2:
    print('\n Calculando la masa...')
    f = int(input('Dame el valor de la fuerza, por favor: '))
    a = int(input('Dame el valor de la aceleración, por favor: '))
    m = f / a
    print(f'El resultado de la masa es: {m}')
elif op == 3:
    print('\n Calculando la aceleracion...')
    f = int(input('Dame el valor de la fuerza, por favor: '))
    m = int(input('Dame el valor de la masa, por favor: '))
    a = f / m
    print(f'El resultado de la aceleracion es: {a}')
else:
    print('Opción invalida :( | Prueba de nuevamente :D)')