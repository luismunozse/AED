# 10. Comisión de Vendedores
# Una empresa debe calcular el total de comisiones que debe abonar por ventas realizadas por sus vendedores,
# para ello le solicita un sistemita que le permita calcular dicho montos.
# Se tiene conocimiento que la empresa tiene cuatro categorías de vendedores (1 a 4). Usted debe solicitar
# el ingreso de la categoría del vendedor y el total de la venta (el proceso termina cuando se ingrese
# una categoría igual a cero) y acumular las comisiones de las ventas rendidas por los vendedores de diferentes en base
# a los siguientes cálculos:
#
# a) Categoría 1: cobra una comisión de 10%
# b) Categoría 2: cobra una comisión de 25%
# c) Categoría 3: cobra una comisión de 30%
# d) Categoría 4: cobra una comisión de 40%
#
# Una vez procesadas todas las ventas mostrar el total de comisiones a pagar por cada categoría de vendedores
# que tiene la empresa junto con el total general

cat = int(input('Ingrese la categoria del vendedor: (1-4) (se corta cuando ingrese 0): '))
comision_cat1 = comision_cat2 = comision_cat3 = comision_cat4 = 0
while cat != 0:
    venta = float(input('Ingrese el monto total de la venta: '))
    if cat == 1:
        comision_cat1 += venta * 0.10
    elif cat == 2:
        comision_cat2 += venta * 0.25
    elif cat == 3:
        comision_cat3 += venta * 0.30
    elif cat == 4:
        comision_cat4 += venta * 0.40
    cat = int(input('Ingrese la categoria del vendedor: (1-4) (se corta cuando ingrese 0): '))
total = comision_cat1 + comision_cat2 + comision_cat3 + comision_cat4

print(f'Total comisiones categoria 1: {comision_cat1}')
print(f'Total comisiones categoria 2: {comision_cat2}')
print(f'Total comisiones categoria 3: {comision_cat3}')
print(f'Total comisiones categoria 4: {comision_cat4}')
print(f'Total General: {total}')