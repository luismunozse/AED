# 1. Ciclistas
# La final de una carrera de ciclistas tiene n competidores (n se ingresa por teclado).
#
# Desarrollar un programa que permita cargar, por cada competidor, nombre y tiempo de carrera. Luego se pide:
#
# a) Determinar y mostrar el nombre del ganador de la carrera.
#
# b) Ingresar por teclado el tiempo record registrado para dicha carrera. Determinar si el tiempo del ganador es menor al tiempo record, mostrar un mensaje.
#
# c) Calcular y mostrar el tiempo promedio entre todos los ciclistas.

tiempo_record = int(input('Ingrese el tiempo record para la carrera en segundos: '))
menor_tiempo = None
suma_tiempo = 0
ganador = None
es_el_primero = True

n = int(input('Ingrese la cantidad de competidores: '))


for i in range(n):
    nombre = input('Ingrese el nombre del ciclista: ')
    tiempo_carrera = int(input('Ingrese el tiempo de carrera en segundos: '))
    if es_el_primero or tiempo_carrera < menor_tiempo:
        menor_tiempo = tiempo_carrera
        ganador = nombre
    suma_tiempo += tiempo_carrera

print(f'El ganador de la carrera es: {ganador}')

if menor_tiempo < tiempo_record:
    print(f'El tiempo del ganador es menor al tiempo record')
else:
    print(f'El tiempo del ganador es mayor al tiempo record')

tiempo_promedio = suma_tiempo/n
print(f'El tiempo promedio entre todos los ciclistas es: {tiempo_promedio} segundos')


