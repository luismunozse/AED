'''
13. Calculo de Precios con Descuento
Una empresa nos solicito un programa que nos permita calcular los precios de los productos que vende al publico
para ello, nuestro programa debe pedir el precio unitario, la cantidad que se vendio y si se pago en efectivo o no.
En base a esto determinar

    1) El Precio final sin descuentos del articulo (precio unitario por cantidad)

    2) Calcular un descuento si el usuario pago en efectivo y la cantidad vendida es superior a 10 unidades del 15% caso contrario solo aplicar un 5% de descuento
'''

print('*' * 25 + 'CALCULADORA DE PRECIOS' + '*' * 25)

precio_unitario = float(input('Ingrese el precio unitario del producto: '))
cantidad = int(input('Ingrese la cantidad vendida: '))
pago = int(input('Ingrese 1-Efectivo 2-Otros Medios de Pago: '))

precio_final = precio_unitario * cantidad
print('Precio final sin descuento: $' + str(precio_final))

if cantidad > 10 and pago == 1:
    precio_final_descuento = precio_final - (precio_final*0.15)
    print('EL precio final con descuento por pago en efectivo y comprar mas de 10 articulos es: $' + str(precio_final_descuento))
else:
    precio_final_descuento = precio_final - (precio_final*0.05)
    print('Precio con descuento del 5%: $' + str(precio_final_descuento))