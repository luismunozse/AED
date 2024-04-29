'''
14. Tarifas de Peaje
La empresa de peajes AED Pase-Pase S.R.L, festeja su séptimo aniversario y, por tal motivo, el día de hoy ofrece premios a a sus clientes.

Estos premios se calculan de la siguiente manera:

1) Cada vez que pasa un cliente, se sortea un número del 0 al 9. Si el número coincide con el último dígito de la patente del vehículo, se le cobra la tarifa promocional de $50,
si no, se le cobra la tarifa estándar de $90

2) Independientemente de la tarifa que deba pagar, si el último dígito de la patente es 7, entonces recibe un descuento del 50%, en caso contrario un descuento del 10%.

Desarrolle un programa en Python que le solicite al usuario los dígitos de su patente (únicamente los dígitos), simule su paso por el peaje e indique el monto a abonar.
'''

import random

patente = input('Ingrese los digitos de la patente del vehiculo: ')

sorteo = random.randint(0,9)
print('El número sorteado es: ' + str(sorteo))
print(patente[len(patente)-1])

if sorteo == int(patente[len(patente) - 1]):
    precio = 50
    print('El numero sorteado coincide con el ultimo digito de la patente. Solo debe pagar: $' + str(precio))
else:
    precio = 90
    print('Tarifa estandar: $' + str(precio))
    if int(patente[len(patente) - 1]) == 7:
        precio = 90- (90 * 0.5)
        print('Felicidades. Su patente finaliza en 7. Solo debe pagar: $' + str(precio))
    else:
        precio = 90 - (90 * 0.1)
        print('Por ser nuestro aniversario igual te llevas un 10% de descuento. Debes abonar: $' + str(precio))

