import random

n = 25000

random.seed(7658)
suma = suma78 = 0
mayor = None
cont500 = cont50027 = cont2710 = cont78 = cont5000 = 0
for i in range(1, n+1):
    num = random.randint(-2500,45000)
    suma += num
    if num <= -500:
        cont500 += 1
    elif -500 < num < 27000:
        cont50027 += 1
    elif num >= 27000 and num % 10 == 0:
        cont2710 += 1
    if num > 0 and (num % 7 == 0 or num % 8 == 0):
        suma78 += num
        cont78 += 1
    if num < 0 and num % 4 == 0:
        if mayor is None or num > mayor:
            mayor = num
    if num < 5000:
        cont5000 += 1


print(suma)
print(cont500,cont50027,cont2710)
promedio = suma78 // cont78
print(promedio)
print(mayor)
porcentaje = cont5000 * 100 // n
print(porcentaje)