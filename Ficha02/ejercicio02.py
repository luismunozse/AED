#2. Descuento en medicinas
#Calcular el descuento y el monto a pagar por un medicamento cualquiera en una
#farmacia (cargar por teclado el precio de ese medicamento) sabiendo que todos los medicamentos
#tienen un descuento del 35%. Mostrar el precio actual, el monto del descuento y el monto final a pagar.

nombre = input('Ingrese el nombre del medicamento: ')
precio = float(input('Ingrese el precio del medicamento: '))

descuento = precio * 0.35

total = precio - descuento

print('Medicamento: ' , nombre , '\nPrecio Actual: ' , precio , '\nDescuento: ', descuento , '\nPrecio final: ' , total)