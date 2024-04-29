'''
10. Terreno
Se ingresan las medidas de frente y fondo de un terreno.

Determinar si es cuadrado o rectangular y calcular su superficie.
'''

frente = float(input('Ingrese la medida del frente del terreno: '))
fondo = float(input('Ingrese la medida del fondo del terreno: '))
superficie = frente * fondo

if(frente == fondo):
    print('El terreno es cuadrado, su superficie mide: ' + str(superficie) + 'metros')
else:
    print('El terreno es rectangular, su superficie mide: ' + str(superficie) + 'metros')