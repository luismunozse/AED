import random

n = 19000

random.seed(3374)
menor = None
suma = div5 = suma123 = suma23 = 0
cont_negativo = cont23 = cont_par_negativo = 0
for i in range(1,n+1):
    num = random.randint(-1000,15000)
    suma += num
    # Punto 1:
    if num < 0:
        cont_negativo += 1
    elif num >= 0 and num < 12000 and num % 5 == 0:
        div5 += 1
    elif num >= 12000 and num % 3 == 0:
        suma123 += num
    # Punto 2:
    if -200 <= num <= 3000:
        suma23 += num
        cont23 += 1
    # Punto 3:
    if num > 0 and num % 9 == 0:
        if menor is None or num < menor:
            menor = num
    # Punto 4:
    if num < 0 and num % 2 == 0:
        cont_par_negativo += 1

print(suma)
promedio = suma23 // cont23
print(cont_negativo,div5,suma123)
print(promedio)
print(menor)
porcentaje = cont_par_negativo * 100 // n
print(porcentaje)
