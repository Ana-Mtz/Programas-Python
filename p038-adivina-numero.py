## El usuario adivina un numero entero al azar entre 1 y 100

import os, random;

while(True):
    os.system('cls')
    print('Adivina cual es el numero secreto c:<\n')
    
    ns = random.randint(1,100)
    i = 0

    while(True):
        n = int(input('Ingresa un numero, por favor: '))
        i+=1
        if n == ns:
            print(f'¡Felicidades! Adivinaste el numero en {i} intentos')
            break
        elif n < ns:
            print('¡Ya casi! El numero secreto es más grande :3')
        else:
            print('¡Alto! El numero secreto es más pequeño :o')
        
    if input('¿Deseas continuar? (S/N): ').upper()=='N': break

print('\nProceso finalizado :) \n')