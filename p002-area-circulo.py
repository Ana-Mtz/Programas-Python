#Calcular el area de un circulo

print('Calcular el area de un circulo')

#sin la biblioteca
print('Dame el radio del circulo')

radio = float(input())

area = 3.1416 * radio * radio

#con la biblioteca
#area = math.pi * math.pw(radio,2)

print(f'El circulo de radio {radio} tiene un area de: {area:,.2f}') #para solo dos decimales

