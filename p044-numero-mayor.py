## Calcular el num mayor de una serie de num introducidos por el teclado
## el proceso se detiene al introducir 0

import os; os.system('cls')
print('Calcular el número mayor y finalizar proceso al ingresar 0')

while True:
    numM = 0 

    while True:
        num = int(input('Por favor, ingresa un número (ingresa 0 para terminar la secuencia): '))

        if num == 0: 
            break

        if num > numM:  
            numM = num

    print(f'\nEl número mayor es: {numM}\n')

    if input('¿Deseas intentar otra vez? (S/N): ').upper() == 'N':  break

print('\nProceso terminado c: ¡Adios!\n')