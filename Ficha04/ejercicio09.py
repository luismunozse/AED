'''
9. Edad mínima
Ingresar por teclado las edades de 3 participantes de un concurso.

Informar si todos cumplen con la edad mínima establecida para el mismo, también ingresada por teclado.
'''

edad_minima = int(input('Bienvenido al concurso. Ingrese la edad minima requerida para participar: '))

print('Ahora ingrese la edad de los participantes: ')

edad1 = int(input('Edad Participante N°1: '))
edad2 = int(input('Edad Participante N°2: '))
edad3 = int(input('Edad Participante N°3: '))

if(edad1 >= edad_minima and edad2 >= edad_minima and edad3 >= edad_minima):
    print('Todos los participantes cumplen con la edad minima requerida para participar en el concurso')
else:
    print('Algun participante o todos no cumplen con la edad para participar')

