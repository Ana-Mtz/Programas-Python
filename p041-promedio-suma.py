## Calcular la suma y el promedio de los num introducidos por el teclado hasta introducir 0
## Contar cuantos numeros se introdujeron
## Repetir el proceso hasta que el usuario lo decida

import os; os.system('cls')
print('Calcular la suma y promedio de los numeros introducidos por el teclado hasta introducir 0')

import os; os.system('cls')
print('Calcular la suma y promedio de números (ingresa 0 para finalizar la secuencia)\n')

while True:
    sum = 0
    totNum = 0

    while True:
        n = int(input('Por favor, ingresa un número (ingresa 0 para terminar la secuencia): '))
        
        if n == 0: break
        
        sum += n
        totNum += 1
        prom = sum / totNum

    print(f'\nSe ingresaron {totNum} numeros en total, dando una suma de {sum} y un promedio de {prom}\n')
    

    if input('¿Deseas continuar? (S/N): ').upper()=='N': break

print('\nProceso finalizado c: \n')