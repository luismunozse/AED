# 6. Menores y promedio
# Realizar un programa que genere 5000 numeros aleatorios en el rango de [0, 100000] y que permita:
#
# Determinar el menor de los numeros generados en forma aleatoria
# Calcular el valor promedio de los números menores a 10.000.

import random

i = suma = 0
menor = None
while i < 5000:
    num = random.randint(0,100000)
    if menor is None or num < menor:
        menor = num
    if num < 10000:
        suma += num
    i += 1
promedio = suma / i

print(f'El menor de los numeros generados es: {menor}')
print(f'El promedio de los numeros menores a 10000 es: {promedio}')

