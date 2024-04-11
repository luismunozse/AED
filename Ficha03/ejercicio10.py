'''
10. Tiempos de Triatlon
Un triatlón es una competición deportiva en que los participantes realizan tres carreras: una de natación, una ciclista
y una pedestre.

Desarrollar un programa que permita ingresar el tiempo (en minutos y segundos) logrados en cada etapa por uno de
los deportistas participantes.

Con esos datos determinar:

Tiempo total de la prueba (en formato hh:mm:ss)
Tiempo máximo y mínimo (en segundos)
Tiempo promedio de la prueba (en segundos, redondeado a 2 decimales)
Consejo: convertir a segundos los horarios ingresados, para facilitar las operaciones
'''

participante = input('Ingrese el nombre del participante: ')
natacion = input('Ingrese el tiempo en mm:ss en natación: ')
ciclismo = input('Ingrese el tiempo en mm:ss en ciclismo: ')
pedestre = input('Ingrese el tiempo en mm:ss en pedestre: ')

minutos_natacion = int(natacion[0:2])
print(minutos_natacion)
segundos_natacion = int(natacion[3:5])
print(segundos_natacion)
tiempo_natacion = (minutos_natacion / 60) + segundos_natacion
minutos_ciclismo = int(ciclismo[0:2])
print(minutos_ciclismo)
segundos_ciclismo = int(ciclismo[3:5])
print(segundos_ciclismo)
tiempo_ciclismo = (minutos_ciclismo / 60) + segundos_ciclismo
minutos_pedestre = int(pedestre[0:2])
print(minutos_pedestre)
segundos_pedestre = int(pedestre[3:5])
print(segundos_pedestre)
tiempo_pedestre = (minutos_pedestre / 60) + segundos_pedestre

tiempo_total = tiempo_natacion + tiempo_ciclismo + tiempo_pedestre
