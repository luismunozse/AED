import random

n = 13000

random.seed(1779)
suma = suma_par = suma_div5 = suma_prom= 0
cont1 = cont_prom = cont_div3 = 0
menor = None
for i in range(1,n+1):
    num = random.randint(-25000,-1000)
    suma += num
    if num % 2 == 0:
        suma_par += num
    if num % 5 == 0:
        suma_div5 += num
    if num >= -2000 and num % 4 != 0:
        cont1 += 1
    if -6000 < num < -2000 and num % 6 != 0:
        suma_prom += num
        cont_prom += 1
    if -20000 <= num <= -5000 and num % 8 == 0:
        if menor is None or num < menor:
            menor = num
    if num > -3000 and num % 3 == 0:
        cont_div3 += 1

print(suma)
print(suma_par,suma_div5,cont1)
promedio = suma_prom//cont_prom
print(promedio)
print(menor)
porcentaje = cont_div3 * 100 // n
print(porcentaje)