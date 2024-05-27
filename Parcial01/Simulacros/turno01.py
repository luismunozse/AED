import random

random.seed(1157)

n = 17000
menor = None
suma = cont1 = cont2 = suma2 = cont3 = suma3 = cont_par = 0

for i in range(1,n+1):
    num = random.randint(1000,37000)
    suma += num
    if num >= 1000 and num < 15000:
        cont1 += 1
    elif num >= 15000 and num < 30000:
        suma2 += num
    elif num >= 30000:
        cont2 += 1
    if num % 7 == 0 and num % 3 != 0:
        cont3 += 1
        suma3 += num
    if num % 2 != 0:
        if menor is None or num < menor:
            menor = num
    else:
        cont_par += 1

promedio = suma3 // cont3
porcentaje = cont_par * 100 // n
print(suma)
print(f'Cantidad de numeros entre [1000;15000): {cont1}')
print(f'Suma de numeros en el intervalo [15000;3000): {suma2}')
print(f'Cantidad de numeros mayores a 30000: {cont2}')
print(f'Promedio entero de los números generados que eran divisibles por 7 pero no por 3: {promedio}')
print(f'Menor de los numeros impares generados: {menor}')
print(f'Porcentaje entero que representa la cantidad de números pares generados sobre la cantidad total de números procesados: {porcentaje}')

