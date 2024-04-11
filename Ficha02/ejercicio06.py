'''
6. Precio de venta
Conociendo el precio de lista de un artículo, determinar:

Precio de venta al contado (10% de descuento)
Precio de venta con tarjeta (5% de recargo)
'''

precio_lista = float(input('Ingrese el precio de lista de algun articulo: '))

precio_contado = precio_lista - (precio_lista * 0.10)
print('Su precio de contado es: ' , precio_contado)

precio_tarjeta = precio_lista + (precio_lista * 0.05)
print('Su precio con tarjeta es: ' ,  precio_tarjeta)



