'''
10. Calculo de Ganancias de Pelicula
Una empresa dedicada al pago de ganancias por las películas que se realizan en los estudios, necesita un sistema que
permita cargar el total que la película recaudó, el nombre del participante de la película que se tiene que abonar,
el porcentaje que se le debe pagar. Con esos datos mostrar el nombre del actor y el monto que recibirá de las ganancias
'''

recaudacion = float(input('Ingrese el total de la recaudación: '))
actor = input('Ingrese el nombre del actor: ')
porcentaje = float(input('Ingrese el porcentaje a pagar por su participación: '))

pago = recaudacion * (porcentaje/100)

print('Actor: ' , actor)
print('Monto a cobrar' , pago)

