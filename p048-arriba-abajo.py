## Imprimir numeros de 1 a n o de n a 1

import os;

while(True):
    os.system('cls')

    print('Imprimir numeros usando ciclo for\n')
    print('[1] Imprimir numeros de 1 a n')
    print('[2] Imprimir numeros de n a 1')
    print('[3] Salir')
    op = int(input('\n¿Qué opción escoges?: '))

    if op == 1:
        print(f'\nImprimir numeros de 1 a n')
        n = int(input('¿Hasta qué numero quieres imprimir?: '))
        for x in range(1, n + 1, 1): print(x, end=' ')
    
    elif op == 2:
        print(f'\nImprimir numeros de n a 1')
        n = int(input('¿Desde donde quieres imprimir?: '))
        for x in range(n, 0, -1): print(x, end=' ')

    if op == 3:
        print('\nTe vamos a extrañar :c'); break
    
    else:
        print('\nEeh... Ingresaste una opción invalida')

    if input('¿Deseas continuar? (S/N): ').upper()=='N': break

print('\nProceso finalizado c:')