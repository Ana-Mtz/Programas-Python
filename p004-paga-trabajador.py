#Calcular la paga total de un trabajador en base a las horas trabajadas y a la paga por hora
#entrada: nombre, horas, paga
#salida: pagabruta(antes de impuesto), impuesto=(paga*tasa), paganeta(despues de impuesto)

print('Calculando la paga de un trabajador \n')

#Entrada de datos
nombre = input('Nombre del trabajador      : ')
horas = int(input('Horas trabajadas        : '))
paga = float(input('Paga por hora trabajada: '))
tasa = 0.03

#Calculando
pagabruta = horas * paga
impuesto = pagabruta * tasa
paganeta = pagabruta - impuesto

#Salida
print('\nResumen de pagos')
print(f'El trabajador {nombre}, trabajo {horas} horas a una paga de {paga} pesos, a una tasa de {tasa} de impuestos')
print(f'Paga bruta (antes de impuestos): {pagabruta:,.2f}')
print(f'Impuesto                       : {impuesto:,.2f}')
print(f'Paga neta (despues de impuesto): {paganeta:,.2f}')