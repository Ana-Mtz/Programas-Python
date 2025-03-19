# Suma numeros hasta dar 100

import os; os.system('cls')

c = 0
s = 0

while c < 200:
    c += 1
    s += c
    print(c, end=' ')
    if s >= 10000:
        print('\n')
        break
else:
    print('\n\n Llegamos a la meta')

print(f'Suma {s}, numeros sumados para alcanzar la meta {c}')
