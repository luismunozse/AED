'''
3. Ecuación de Einstein
La famosa ecuación de Einstein para conversión de una masa m en energía viene dada por la fórmula:

E = mc2

Donde c es la velocidad de la luz cuyo valor es c = 299792.458 km/seg.
Desarrolle un programa que lea el valor una masa m en kilogramos y obtenga la cantidad de energía E
producida en la conversión.'''

c = 299792.458

m = float(input('Ingrese el valor de la masa en kilogramos: '))

e = m * (c**2)

print('Energia: ', e , 'kg(km/seg)2')

