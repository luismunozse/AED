import random

# cantidad de numeros a generar:
n = 14000

#semilla
random.seed(973)

suma = suma915 = m11 = m1117 = m17 = div3 = div6 = div8 = c915 = 0
mayor = None

for i in range(1, n+1):
    num = random.randint(100,21100)
    suma += num
    # Punto 1:
    if num <= 11000:
        m11 += 1
    elif num > 11000 and num < 17000:
        if num % 3 == 0 and num % 8 == 0:
            m1117 += 1
    elif num >= 17000:
        m17 += 1
    # Punto 2:
    if num % 9 == 0 and num <= 15000:
        suma915 += num
        c915 += 1
    # Punto 3:
    if 1000 <= num <= 14000:
        if mayor is None or num > mayor:
            mayor = num
    # Punto 4:
    if num % 6 == 0:
        div6 += 1

promedio = suma915 // c915
porcentaje = div6 * 100 // n
print(suma)
print(f'menores o iguales que 11000: {m11}')
print(f'mayores que 11000 pero menores que 17000 y además eran divisibles por 3 y por 8 al mismo tiempo: {m1117}')
print(f'mayores o iguales que 17000: {m17}')
print(f' promedio entero de todos los números generados que sean divisibles por 9 pero que sean también menores o iguales a 15000: {promedio}')
print(f'mayor entre todos los números generados cuyo valor esté entre 1000 y 14000 (includos ambos): {mayor}')
print(f'porcentaje entero que la cantidad de números divisibles por 6 representa sobre la cantidad total de números: {porcentaje}%')