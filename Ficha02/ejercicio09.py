'''
9. Datos de un rectángulo
Hacer un programa que tome como entrada el ancho y el alto de un rectángulo y determine el perímetro y la superficie del mismo.
'''

ancho = float(input('Ingrese el ancho del rectangulo: '))
alto = float(input('Ingrese el alto del rectangulo: '))

perimetro = 2*ancho + 2*alto
print('El perimetro del rectangulo es: ' , perimetro)

superficie = ancho * alto
print('La superficie del rectangulo es: ', superficie)