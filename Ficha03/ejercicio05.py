'''
5. Control electoral
Desarrollar un programa de control electoral en un centro vecinal, en el que se ingresen, para cierto candidato:
apellido, nombre y cantidad de votos. Luego presentar en pantalla un resumen que muestre: iniciales del candidato,
cantidad de votos entre paréntesis, y debajo una línea con tantas  "x" como votos obtenidos (por ejemplo, el candidato
obtuvo 4 votos, deberá aparecer una línea como esta:  "xxxx"  con cuatro letras "x") (Asumimos que en el centro vecinal
no hay demasiados electores, de forma que podamos estar seguros que no habrá miles o millones de votos... sólo unos
pocos para darle sentido al enunciado).
'''

print('*' * 50)
print('Programa de Control Electoral')
print('*' * 50)

print('****** Datos del candidato ******')
apellido = input('Ingrese el apellido del candidato: ')
nombre = input('Ingrese el nombre del candidato: ')
votos = int(input('Ingrese la cantidad de votos que obtuvo el candidato: '))

ini_ape = apellido[0]
ini_nom = nombre[0]
cant_votos = 'x' * votos

print('****** Resumen ******')
print('Candidato: ', ini_nom, ini_ape, '\nCantidad de votos: ' , cant_votos)


