# 2. Ventas por sucursal
# Ingresar una serie de números por teclado que representan la cantidad de ventas realizadas en las diferentes sucursales de un país de una determinada empresa.
#
# Los requerimientos funcionales del programa son:
#
# a) Informar la cantidad de ventas ingresadas.
#
# b) Total de ventas.
#
# c) Cantidad de ventas cuyo valor este comprendido entre 100 y 300 unidades.
#
# d) Cantidad de ventas con 400, 500 y 600 unidades.
#
# e) Indicar si hubo una cantidad de ventas inferior a 50 unidades.
#
# Usted deberá ingresar cantidades de ventas hasta que se ingrese un valor negativo.

ventas = cont_ventas = cont1 = cont2 = cont400 = cont500 = cont600 = suma = 0
ventas_menor_50 = False
ventas = int(input('Ingrese la cantidad de ventas realizada en la sucursal: '))
while ventas > 0:
    ventas = int(input('Ingrese la cantidad de ventas realizada en la sucursal: '))
    if ventas >= 100 and ventas <= 300:
        cont1 += 1
    if ventas == 400:
        cont400 += 1
    if ventas == 500:
        cont500 += 1
    if ventas == 600:
        cont600 += 1
    if ventas < 50:
        ventas_menor_50 = True
    suma += ventas
    cont_ventas += 1

print(f'Cantidad de ventas ingresadas: {cont_ventas} ventas')
print(f'Total de las ventas: {suma}')
print(f'Ventas comprendidas entre 100 y 300 unidades: {cont1}')
print(f'Ventas de 400 unidades: {cont400}')
print(f'Ventas de 500 unidades: {cont500}')
print(f'Ventas de 600 unidades: {cont600}')
print(f'Ventas menores a 50 unidades?: {ventas_menor_50}')

