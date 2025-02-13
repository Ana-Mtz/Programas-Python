#Calcular la hipotenusa de un triangulo rectangulo
#yo usé la libreria de math para practicar

import math as m #para poder usar las funciones de la libreria y hacer la ecuación más facil :D
import os; os.system('cls')

print('Calular la hipotenusa de un triangulo rectangulo dadas las longitudes de sus lados.')

print('Por favor, dame la medida de los lados, separadas por un espacio: ')
l1, l2 = input().split() #input para introducir las medidas y el split para separar la cadena en base a los espacios
l1, l2 = int(l1), int(l2) #primero me dio error porque debí ponerlos como enteros para poder elevarlos

#la hipotenusa es c=raizcu(a^2 + b^2)
hip = m.sqrt(m.pow(l1, 2) + m.pow(l2, 2))

print(f'La hipotenusa resultante es: {hip}')