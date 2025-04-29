## Simular u registro de calificaciones usando un diccionario, sacamos el promedio
## realizamos cambios y actializaciones

import os; os.system('cls')

materias = ['Fisica', 'Quimica', 'Matematicas', 'Geografia', 'Estadistica']
califs = {10, 9, 8, 7.5, 6}

print(f'Lista de materias : {materias} - {len(materias)}')
print(f'Lista de califs: {califs} - {len(califs)}')

notas = dict (zip(materias, califs))

print(f'\nEl diccionario completo de nota es: {notas} - {len(notas)}')

## Agregar
notas.update({'Ingles':10,'Programacion':7})
print(f'\nEl diccionario es {notas} - {len(notas)}')

## Remover
notas.pop('Fisica')
notas.popitem()
print(f'\nEl diccionario es {notas} - {len(notas)}')

## Modificar
notas['Quimica'] = 10
notas.update({'Matematicas':10})
print(f'\nEl diccionario es {notas} - {len(notas)}')

## Mostrar la lista de materias y calificaciones, asi como el promedio
s = 0
print('\nMaterias y calificaciones')
for m, c in notas.items():
    print(f'{m:<12} - {c:5}')
    s = s + c

p = s / len(notas)

print(f'La suma es {s} el promedio es {p}')

## Limpiar
notas.clear()
print(f'\nEl diccionario es {notas} - {len(notas)}')