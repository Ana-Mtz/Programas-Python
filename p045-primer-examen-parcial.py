## Se desea llevar el control de la inscripción a un evento académico
## de la Universidad Munchis.
## Se especifica: tipo de usuario, paquete y cantidad.
## Hay que calcular el subtotal de la venta, sumando el precio del tipo
## mas el precio de tipo de paquete y multiplicando por la cantidad solicitada
## Se otorgará un descuendo si el subtotal es mayor a 5 mil y de acuerdo a
## lo siguiente: alumno (20%), trabajador (10%) y docente (5%)
## Finalmente, se muestra un resumen de los datos de venta y el 
## total de venta del día.

import os; os.system('cls')

print('Universidad Munchis SA de CV')

tot_vent = 0


while(True):
    print('\nSistema de Inscripción a un evento académico \n')

    tipUsu = int(input('Introduce que tipo de usuario eres, por favor: Alumno-$100 [1], Trabajador-$200 [2], Docente-$500 [3]: '))
    #tipPaq = input('Introduce el tipo de paquete que deseas: Solo conferencias $600 [1], Con eventos sociales $800 [2], Con kit de acceso $900 [3] ')
    #cant = input('¿Cuantos paquetes quieres solicitar?: ')

    if tipUsu == 1:
        alu = 100
        tipPaq = int(input('\nIntroduce, por favor, el tipo de paquete que deseas: Solo conferencias-$600 [1], Con eventos sociales-$800 [2], Con kit de acceso-$900 [3]: '))
    
        if tipPaq == 1:
            paq1 = 600
            cant = int(input('\n¿Cuantos paquetes quieres solicitar?: '))

            subtotal = (alu + paq1) * cant
            if subtotal >= 5000:
                desc = subtotal * 0.20
                tf = subtotal - desc
                print(f'\nSu subtotal es de: ${subtotal}, pero tiene un descuento de ${desc}. Su total final es de: ${tf} \n')
            else:
                tf = subtotal
                print(f'\nSu total es de: ${subtotal} \n')
            tot_vent += tf

        elif tipPaq == 2:
            paq2 = 800
            cant = int(input('\n¿Cuantos paquetes quieres solicitar?: '))

            subtotal = (alu + paq2) * cant
            if subtotal >= 5000:
                desc = subtotal * 0.20
                tf = subtotal - desc
                print(f'\nSu subtotal es de: ${subtotal}, pero tiene un descuento de ${desc}. Su total final es de: ${tf} \n')
            else:
                tf = subtotal
                print(f'\nSu total es de: ${subtotal} \n')
            tot_vent += tf

        elif tipPaq == 3:
            paq3 = 900
            cant = int(input('\n¿Cuantos paquetes quieres solicitar?: '))

            subtotal = (alu + paq3) * cant
            if subtotal >= 5000:
                desc = subtotal * 0.20
                tf = subtotal - desc
                print(f'\nSu subtotal es de: ${subtotal}, pero tiene un descuento de ${desc}. Su total final es de: ${tf} \n')
            else:
                tf = subtotal
                print(f'\nSu total es de: ${subtotal} \n')
            tot_vent += tf

#~~~~~~~~~~~~~~~~~~

    elif tipUsu == 2:
        trab = 200
        tipPaq = int(input('\nIntroduce, por favor, el tipo de paquete que deseas: Solo conferencias-$600 [1], Con eventos sociales-$800 [2], Con kit de acceso-$900 [3]: '))
    
        if tipPaq == 1:
            paq1 = 600
            cant = int(input('\n¿Cuantos paquetes quieres solicitar?: '))

            subtotal = (trab + paq1) * cant
            if subtotal >= 5000:
                desc = subtotal * 0.10
                tf = subtotal - desc
                print(f'\nSu subtotal es de: ${subtotal}, pero tiene un descuento de ${desc}. Su total final es de: ${tf} \n')
            else:
                tf = subtotal
                print(f'\nSu total es de: ${subtotal} \n')
            tot_vent += tf

        elif tipPaq == 2:
            paq2 = 800
            cant = int(input('\n¿Cuantos paquetes quieres solicitar?: '))

            subtotal = (trab + paq2) * cant
            if subtotal >= 5000:
                desc = subtotal * 0.10
                tf = subtotal - desc
                print(f'\nSu subtotal es de: ${subtotal}, pero tiene un descuento de ${desc}. Su total final es de: ${tf} \n')
            else:
                tf = subtotal
                print(f'\nSu total es de: ${subtotal} \n')
            tot_vent += tf

        elif tipPaq == 3:
            paq3 = 900
            cant = int(input('\n¿Cuantos paquetes quieres solicitar?: '))

            subtotal = (trab + paq3) * cant
            if subtotal >= 5000:
                desc = subtotal * 0.10
                tf = subtotal - desc
                print(f'\nSu subtotal es de: ${subtotal}, pero tiene un descuento de ${desc}. Su total final es de: ${tf} \n')
            else:
                tf = subtotal
                print(f'\nSu total es de: ${subtotal} \n')
            tot_vent += tf

#~~~~~~~~~~~~~~~~~~~~~
    elif tipUsu == 3:
        doc = 500
        tipPaq = int(input('\nIntroduce, por favor, el tipo de paquete que deseas: Solo conferencias-$600 [1], Con eventos sociales-$800 [2], Con kit de acceso-$900 [3]: '))
    
        if tipPaq == 1:
            paq1 = 600
            cant = int(input('\n¿Cuantos paquetes quieres solicitar?: '))

            subtotal = (doc + paq1) * cant
            if subtotal >= 5000:
                desc = subtotal * 0.05
                tf = subtotal - desc
                print(f'\nSu subtotal es de: ${subtotal}, pero tiene un descuento de ${desc}. Su total final es de: ${tf} \n')
            else:
                tf = subtotal
                print(f'\nSu total es de: ${subtotal} \n')
            tot_vent += tf

        elif tipPaq == 2:
            paq2 = 800
            cant = int(input('\n¿Cuantos paquetes quieres solicitar?: '))

            subtotal = (doc + paq2) * cant
            if subtotal >= 5000:
                desc = subtotal * 0.05
                tf = subtotal - desc
                print(f'\nSu subtotal es de: ${subtotal}, pero tiene un descuento de ${desc}. Su total final es de: ${tf} \n')
            else:
                tf = subtotal
                print(f'\nSu total es de: ${subtotal} \n')
            tot_vent += tf

        elif tipPaq == 3:
            paq3 = 900
            cant = int(input('\n¿Cuantos paquetes quieres solicitar?: '))

            subtotal = (doc + paq3) * cant
            if subtotal >= 5000:
                desc = subtotal * 0.05
                tf = subtotal - desc
                print(f'\nSu subtotal es de: ${subtotal}, pero tiene un descuento de ${desc}. Su total final es de: ${tf} \n')
            else:
                tf = subtotal
                print(f'\nSu total es de: ${subtotal} \n')
            tot_vent += tf
#~~~~~~~~~~~~~~~~~~

    if input('\n¿Deseas continuar? (S/N): ').upper()=='N': break

print(f'\nTotal de ventas: ${tot_vent}') 
print('\nProceso finalizado :) \n')