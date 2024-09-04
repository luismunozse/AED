# 1. Estudio climatológico
# Como parte de un estudio climatológico, se desea un programa que permita obtener una serie de estadísticas a partir de un conjunto de muestras de temperatura.
#
# Se pide un programa que:
#
# Ingrese n muestras de temperatura, donde cada muestra contiene la temperatura registrada, la región donde se registró la misma (1-20), y el día del mes en el que se registró la temperatura
# Determinar el promedio general de temperatura
# Dada una región, mostrar las temperaturas de la misma, ordenadas por dia, de menor a mayor
# Dada una región, determinar si la temperatura de alguna muestra superó el valor x, ingresado por teclado.
# Determinar la cantidad de muestras por region (20 contadores)

def cargar_datos():
    n = int(input('Ingrese la cantidad de muestras a procesar: '))
    temperaturas = [0.0] * n
    regiones = [0] * n
    dias = [0] * n
    for i in range(n):
        

def menu():
    print('1 - Cargar datos')
    print('2 - Promedio de temperaturas')
    print('3 - Mostrar  por region')
    print('4 - Buscar temperaturas mayores a x')
    print('5 - Mostrar cantidad de muestras por region')
    print('0 - Salir')

def principal():
    pass


if __name__ == '__main__':
    principal()