# 4. Promedio de números aleatorios
# Realice un programa que permita calcular el promedio de 1000 números aleatorios generados en el rango de [0, 100000]

import random

i = suma = promedio = 0

while i < 1000:
    num_aleatorio = random.randint(0,100000)
    suma += num_aleatorio
    i += 1

promedio = suma / i

print(f'El promedio de 1000 numeros aleatorios generados en el ranfo de [0,100000] es: {promedio}')
