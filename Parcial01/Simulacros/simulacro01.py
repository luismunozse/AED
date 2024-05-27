import random

random.seed(49)

n = 20000

suma = 0
div5 = div7 = div9 = 0
mayor = None
cant_par = 0

for i in range(n):
    num = random.randint(1, 45000)
    suma += num
    if num % 5 == 0:
        div5 += 1
    if num % 7 == 0:
        div7 += 1
    if num % 9 == 0:
        div9 += 1
    if num % 10 >= 5 and num % 10 <= 8:
        if mayor is None or num > mayor:
            mayor = num
    if num < 15000:
        if num % 2 == 0:
            cant_par += 1

print(suma)
print(f'Multiplos de 5: {div5}')
print(f'Multiplos de 7: {div7}')
print(f'Multiplos de 9: {div9}')
print(f'Mayor cuyo ultimo digito es mayor o igual a 5 y menor o igual a 8: {mayor}')
print(f'Cantidad de numeros pares generados que son menor a 15000: {cant_par}')

porcentaje = (cant_par * 100) // n

print(f'Porcentaje entero que representan los números pares menores a 15000 respecto del total de números procesados: {porcentaje}%')


