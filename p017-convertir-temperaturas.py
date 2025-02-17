#Convertir temperatura de F a C y viceversa

import os; os.system('cls')

print('#Convertir temperatura de F a C y viceversa')
print('De centigrados a Farenheit .... [1]')
print('De Farenheit a centigrados .... [2]')

op = int(input('Elige una opción: '))

if op == 1:
    print('Convirtiendo de C a F ...')
    temp = float(input('Grados C a convertir: '))
    res = (temp * 9 /5) + 32
    print(f'{temp}C, equivalen a {res} grados F')
else:    
    print('Convirtiendo de F a C ...')
    temp = float(input('Grados F a convertir: '))
    res = (temp - 32) * 5/9
    print(f'{temp}F, equivalen a {res} grados C')
