## Imprimir una piramide de caracteres

import os

while(True):
    os.system('cls')

    ren = int(input('¿De cuantos renglones quieres tu piramide?: '))
    car = input('¿De qué caracter sera tu piramide?: ')

    for i in range(1, ren + 1):
        for j in range(1, i + 1):
            print(car, end='')
        print()
    
    if input('\n¿Deseas intentarlo de nuevo? (S/N): ').upper()=='N': break

print('\nProceso finalizado :D')