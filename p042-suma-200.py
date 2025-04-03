
## Calcular la suma de los num inroducidos por el usuario hasta que la sum sea mayor igual a 200
## luego mostrar cuantos num se introdujeron y la suma de los mismos

import os; os.system('cls')
print('Calcular la suma de los numeros introducidos y detenerla si el resultado es mayor igual a 200')

while(True):
    num = 0
    sum = 0
    totNum = 0

    while sum < 200:
        num = int(input('Por favor, introduce un numero: '))
        sum += num
        totNum += 1

    print(f'\nSe ingresaron {totNum} numeros en total, dando una suma de {sum}\n')

    if input('¿Deseas continuar? (S/N): ').upper()=='N': break


print('\nProceso terminado c: \n')