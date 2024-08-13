# 1. Pluviómetro
# Se ha solicitado un programa que permita cargar las precipitaciones promedio en cada mes del país, en base a esos datos armar un menú de opciones que permita:
#
# Determinar el promedio anual de lluvias
# Determinar el promedio de lluvias para un determinado trimestre
# Determinar el mes más seco del año
# Determinar los meses del año en los que llovió más que el promedios de lluvia de to-do el año.

import random

def validar_rango(lim_ini, lim_fin, mensaje = 'Ingrese un número: '):
    numero = lim_ini - 1
    while numero < lim_ini or numero > lim_fin:
        numero = int(input(mensaje))
        if numero < lim_ini or numero > lim_fin:
            print(f'Opción incorrecta. Debe estar comprendido entre {lim_ini} y {lim_fin} incluidos')
        return numero


def promedio_anual(lluvias):
    suma = 0
    tam = len(lluvias)
    for lluvia_mensual in lluvias:
        suma += lluvia_mensual
    return suma/tam


def promedio_sub_vector(vec, ind_desde, ind_hasta):
    suma = 0
    cantidad = ind_hasta - ind_desde + 1
    for i in range(ind_desde,ind_hasta):
        suma += vec[i]
    promedio = suma / cantidad
    return promedio


def determinar_promedio_trimestre(lluvias):
    trimestre = validar_rango(1,4, ' Ingrese el trimestre a calcular: ')
    ind_inicial = (trimestre - 1) * 3
    promedio_trimestral =

def principal():
    menu = 'Menu de Opciones: \n' \
            '1 - Determinar el promedio anual de lluvias \n' \
            '2 - Determinar el promedio de lluvias para un determinado trimestre \n' \
            '3 - Determinar el mes más seco del año \n' \
            '4 - Determinar los meses del año en los que llovió más que el promedios de lluvia de todo el año \n' \
            '5 - Mostrar lluvias anuales: \n' \
            '0 - Salir' \
            'Ingrese su opción: '

    opcion = -1

    lluvias = [0] * 12
    for i in range(len(lluvias)):
        lluvias[i] = random.randrange(45.8, 160.1)

    while opcion != 0:
        opcion = validar_rango(0,5,menu)
        if opcion == 1:
            prom = promedio_anual(lluvias)
            print(f'El promedio anual de lluvias en el pais fue {prom} lluvias')
        if opcion == 2:







if __name__ == '__main__':
    principal()