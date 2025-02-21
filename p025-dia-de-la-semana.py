#Dado un numero entre 1 y 7, mostrar con letra el dia de la semana correspondiente

import os; os.system('cls')

print('Imprimir el dia de la semana, segun el numero entero ingresado :3')

dia_semana = int(input('Por favor, ingresa el numero del dia de la semana que quieres mostrar en pantalla: '))

if dia_semana == 1:
    print('El dia de la semana es: Lunes')
elif dia_semana == 2:
    print('El dia de la semana es: Martes')
elif dia_semana == 3:
    print('El dia de la semana es: Miercoles')
elif dia_semana == 4:
    print('El dia de la semana es: Jueves')
elif dia_semana == 5:
    print('El dia de la semana es: Viernes')
elif dia_semana == 6:
    print('El dia de la semana es: Sabado')
elif dia_semana == 7:
    print('El dia de la semana es: Domingo')
else:
    print('Numero invalido, por favor intenta nuevamente')