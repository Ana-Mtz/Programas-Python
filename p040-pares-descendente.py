## Imprimir los numeros pares desde 100 hasta el numero que decida el usuario
## Imprimir la suma de esos numeros pares

import os; os.system('cls')
print('Imprimir los numeros pares desde 100 hasta que el usuario indica \n')

n = 100
sum = 0

while(True):
    numf = int(input('Ingresa, por favor, hasta que numero quieres imprimir: '))

    if numf > 100:
        while n < numf:
            n = n + 1
            if n % 2 == 0:
                print(n)
                sum += n

        if input('¿Deseas continuar? (S/N): ').upper()=='N': break
    else:
        print('\nEl valor debe ser mayor a 100 :( | Intenta de nuevo c:\n')

print(f'\nLa suma de los numeros impares es: {sum}')
        
print('\nProceso finalizado c: \n')