#Ejemplifica las operaciones matemáticas básicas

import os; os.system('cls')

#datos de prueba
#x = 10.5
#y = 2.5

x = float(input('Valor de x: '))
y = float(input('Valor de y: '))

suma = x + y
resta = x - y
multi = x * y
div = x / y
residuo = x % y
pot = x ** y
dive = x // y

print(f'Suma: {suma}\n Resta: {resta}\n Multiplicacion: {multi}\n División: {div}')
print(f'Residuo: {residuo}\n Potencia: {pot}\n División entera: {div}')
