## Calcular la temperatura convertida de grados C a F de un rango de valores
## introducido por el usuario. Introduce la temp inicial y la temp final en grados
## centigrados y el programa realiza la conversion incrementando el valor 

import os; os.system('cls')
print('Calcular la temperatura convertida de grados C a F de un rango de valores')

while(True):
    tempI = int(input('Introduce, por favor, los grados °C iniciales a convertir: '))
    tempF = int(input('Ahora, por favor, grados °C hasta donde quieres convertir: '))
    celcius = tempI

    while celcius <= tempF:
        far = ((celcius * (9 / 5)) + 32)
        print(f'{celcius}°C\t->\t{far:.2f}°F')

        celcius += 1

    if input('¿Deseas continuar? (S/N): ').upper()=='N': break

print('\nProceso terminado c: ¡Adios! \n')