'''
11. Galería de arte
Una galería de arte desea preparar un catálogo de sus cuadros más famosos.

Se realiza una prueba con tres cuadros y por cada uno se ingresa el año en que fue creado. El programa deberá:

Verificar si todos los cuadros son anteriores al siglo XX (El siglo XX es el siglo pasado. Se inició en el año 1901 y
terminó en el año 2000).
Determinar si alguna de las obras fue creada en un año que se ingresa por teclado.
Informar la diferencia en años entre la obra más nueva y la más antigua.
'''

c1 = int(input('Año de creacion del primer cuadro: '))
c2 = int(input('Año de creacion del segundo cuadro: '))
c3 = int(input('Año de creacion del tercer cuadro: '))

if c1 <= 1901 and c2 <= 1901 and c3 <= 1901:
    print('Todos los cuadros son anteriores al siglo XX')
else:
    print('No todos los cuadros son anteriores al siglo XX')

anio = int(input('Ingrese el año a buscar: '))

if c1 == anio or c2 == anio or c3 == anio:
    print('Existen cuadros para el año: ' + str(anio))
else:
    print('No existen resultados para el año ingresado')

if c1 > c2 and c1 > c3:
    mayor = c1
    if c2 > c3:
        menor = c3
    else:
        menor = c2
else:
    if c2 > c3 and c3 > c1:
        mayor = c2
        menor = c1
    else:
        mayor = c3
        menor = c2

dif = mayor - menor

print('La diferencia en años de la obra mas nueva con la mas antigua es de: ' + str(dif) + ' años')
