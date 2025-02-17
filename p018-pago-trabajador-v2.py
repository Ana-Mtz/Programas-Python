#Calcular la paga de un trabajador considerando que las horas extras se pagan al doble

import os; os.system('cls')

print('Calcular la paga de un trabajador considerando que las horas extras se pagan al doble')

nombre = input('Nombre del trabajador: ')
horas = int(input('Horas trabajadas: '))
paga = float(input('Paga por hora: '))

extra = pextra = total = 0

if horas > 40:
    extra = horas - 40
    pextra = extra * (2 * paga)
    total = (40 * paga) + pextra
else:
    total = paga * horas

print(f'{nombre} trabajo {horas}, con una paga de {paga} pesos, pago extra {pextra} pesos, pago total {total}')
