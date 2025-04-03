## Imprimir los numeros impares de forma ascendente hasta que el usuario decida
## Imprimir la suma de esos numeros impares

import os; os.system('cls')
print('Imprimir los numeros de forma ascendente hasta que el usuario decida \n')

n = 0
sum = 0

while(True):
    numf = int(input('Ingresa, por favor, hasta que numero quieres imprimir: '))

    while n < numf:
        n = n + 1
        if n % 2:
            print(n)
            sum += n

    if input('¿Deseas continuar? (S/N): ').upper()=='N': break

print(f'\nLa suma de los numeros impares es: {sum}')
        
print('\nProceso finalizado c: \n')