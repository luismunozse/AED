# 3. Menú y números aleatorios
# Realice un programa que le ofrezca al usuario un menú de opciones que le permita ejecutar las siguientes acciones:
#
# Opción 1: Calcular promedio de 1.000 números aleatorios generados en el rango de [0, 100.000].
#
# Opción 2: Buscar el mayor de 10.000 números aleatorios generados en el rango de [0, 100.000].
#
# Opción 3: Buscar el menor de 5.000 números aleatorios generados en el rango de [0, 100.000] y calcular el valor promedio de los números menores a 10.000.
#
# Cualquier otro número: Salir del programa.

import random

suma = i = promedio = prom10 = sum10 = mayor = 0
menor = 100000
print('Opción 1: Calcular promedio de 1.000 números aleatorios generados en el rango de [0, 100.000].')
print('Opción 2: Buscar el mayor de 10.000 números aleatorios generados en el rango de [0, 100.000].')
print('Opción 3: Buscar el menor de 5.000 números aleatorios generados en el rango de [0, 100.000] y calcular el valor promedio de los números menores a 10.000.')
opcion = int(input('Elija su opcion (1-2-3): '))
if opcion > 0 and opcion <= 3:
    if opcion == 1:
        while i < 1000:
            num_aleatorio = random.randint(0, 100000)
            suma += num_aleatorio
            i += 1
        promedio = suma / i
        print(f'Promedio de 1000 numeros entre 0 y 100000: {promedio}')
    elif opcion == 2:
        while i < 10000:
            num_aleatorio = random.randint(0, 100000)
            if num_aleatorio > mayor:
                mayor = num_aleatorio
            i += 1
        print(f'Mayor de 10000 numeros aleatorios entre 0 y 100000: {mayor}')
    else:
        while i < 5000:
            num_aleatorio = random.randint(0, 100000)
            if menor > num_aleatorio:
                menor = num_aleatorio
            if num_aleatorio < 10000:
                sum10 += num_aleatorio
            i += 1
        prom10 = sum10/i
        print(f'Menor de 5000 numeros aleatorios entre 0 y 100000: {menor}')
        print(f'Promedio de los numeros menores a 10000: {prom10}')








