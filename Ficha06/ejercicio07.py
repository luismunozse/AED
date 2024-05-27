# 7. Números pares e impares
# Se pide desarrollar un programa que permita leer una serie de números. La finalización de carga de datos se presenta cuando el usuario ingrese un número negativo.
#
# Los requerimientos funcionales del programa son:
#
# a) La sumatoria de solo los números que estén comprendidos entre 50 y 100.
#
# b) Cantidad de valores pares ingresados.
#
# c) Cantidad de valores impares ingresados.
#
# d) Informar si en la carga de números se ingreso al menos un número 0.
#
# e) Informar si la serie contiene solo números pares e impares alternados

num = int(input('Ingrese un numero (si es negativo, se corta): '))
sum = cont_par = cont_impar = cont0 = 0
num_alternado = True
ultima_paridad = None
while num >= 0:
    if num >= 50 and num <= 100:
        sum += num
    if num % 2 == 0:
        paridad_actual = 'par'
        cont_par += 1
    else:
        paridad_actual = 'impar'
        cont_impar += 1
    if num == 0:
        cont0 += 1
    if ultima_paridad is not None and ultima_paridad == paridad_actual:
        num_alternado = False
    ultima_paridad = paridad_actual
    num = int(input('Ingrese un numero (si es negativo, se corta): '))

print(f'La suma de los numeros comprendidos entre 50 y 100 es: {sum}')
print(f'Cantidad de valores pares ingresados: {cont_par}')
print(f'Cantidad de valores impares ingresados: {cont_impar}')
if cont0 > 0:
    print('A menos se ingreso un cero')
else:
    print('No se ingreso un cero')
if num_alternado:
    print('La serie contiene numeros pares e impares alternados')
else:
    print('La serie no contiene numeros pares e impares alternados')