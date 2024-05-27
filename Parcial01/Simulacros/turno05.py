import random

n = 30000

random.seed(2753)
menor = None
suma = suma1 = suma_neg35 = 0
cont_negativo = cont5000_impar = cont_neg35 = cont_neg_impar = 0
for i in range(1,n+1):
    num = random.randint(-15000,15000)
    suma += num
    if num < 0:
        cont_negativo += 1
    elif 0 <= num < 5000:
        suma1 += num
    elif num >= 5000 and num % 2 != 0:
        cont5000_impar += 1
    if num < 0 and (num % 3 == 0 and num % 5 == 0):
        suma_neg35 += num
        cont_neg35 += 1
    if num > 0 and (num % 3 == 0 and num % 4 != 0):
        if menor is None or num < menor:
            menor = num
    if num < 0 and num % 2 != 0:
        cont_neg_impar += 1

print(suma)
print(cont_negativo,suma1,cont5000_impar)
promedio = suma_neg35 // cont_neg35
print(promedio)
print(menor)
porcentaje = cont_neg_impar * 100 // n
print(porcentaje)