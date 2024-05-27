import random

random.seed(20220512)

n = 25000

suma = div3 = div5 = no_div = acu = cont = 0
mayor = None

for i in range(n):
    num = random.randint(1,45000)
    suma += num
    if num % 3 == 0:
        div3 += 1
    elif num % 5 == 0:
        div5 += 1
    else:
        no_div += 1
    if str(num)[0] == '1':
        if mayor is None or num > mayor:
            mayor = num
    if num % 2 == 0 and num % 11 == 0:
        acu += num
        cont += 1

print(suma)

print(div3,div5,no_div)

promedio = acu//cont
print(promedio)

print(mayor)

porcentaje_div3 = div3 * 100 // n
porcentaje_div5 = div5 * 100 // n
porcentaje_no_div = no_div * 100 // n

print(porcentaje_div3,porcentaje_div5,porcentaje_no_div)
