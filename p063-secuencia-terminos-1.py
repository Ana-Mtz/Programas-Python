## Imprimir la secuencia de los terminos armonicos el numero de renglones
## que el usuario desee y su suma

import os; os.system('cls')

print('Imprimir la secuencia de los terminos armonicos el numero de renglones :D')

n = int(input('Por favor, indica cuantos terminos deseas: '))
sum = 0

for i in range(1, n + 1):
    if i==1:
        print("1+",end=" ")
        sum+=1
    elif i==n:
        print(f"1/{i}!",end=" ")
        sum+=(1/i)
    else:
        print(f'1/{i}!',end='+')
        sum+=(1/i)

print(f'\nLa suma de los terminos armonicos es: {sum}')