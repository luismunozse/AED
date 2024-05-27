# 5. Busqueda de mayor
# Realizar un programa que permita buscar el mayor de 10.000 números aleatorios generados en el rango de [-100.000, 100.000].
# Además de informar el mayor, debe informar el porcentaje que representan los números positivos sobre el total de números generados.

import random

i = may = cont = 0
while i < 10000:
    num = random.randint(-100000,100000)
    if num > may:
        may = num
    if num > 0:
        cont += 1
    i += 1

porcentaje = (cont * 100) / i
print(f'El mayor de 10000 numeros aleatorios generados en el rango [-100000,100000] es: {may}')
print(f'El porcentaje que representan los numeros positivos sobre el total de numeros generados es: {porcentaje}%')
