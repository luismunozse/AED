'''
1. Complejo de cines
Desarrollar un programa que permita procesar funciones de un complejo de cines. Por cada función se conoce: cantidad de
espectadores y descuento (S/N). La carga termina cuando la cantidad de espectadores sea igual a 0 (cero).

El programa deberá:

a) Calcular la recaudación total del complejo, considerando que el valor de la entrada es de $50 en los días con
descuento y $75 en los días sin descuento.

b) Determinar cuántas funciones con descuento se efectuaron y qué porcentaje representan sobre el total de funciones.
'''

funciones = 3
esp_func1 = int(input('Ingrese la cantidad de espectadores para la funcion 1: '))
descuento = input('Tiene descuento? (S/N): ')
esp_func2 = int(input('Ingrese la cantidad de espectadores para la funcion 2: '))
descuento = input('Tiene descuento? (S/N): ')
esp_func3 = int(input('Ingrese la cantidad de espectadores para la funcion 3: '))
descuento = input('Tiene descuento? (S/N): ')
espectadores = esp_func1 + esp_func2 + esp_func3
rec_desc = 0
while(espectadores != 0):
    if(descuento == 's' or descuento == 'S'):
        recaudacion = espectadores * 50
        rec_desc += 1
    else:
        recaudacion = espectadores * 75

print('Funciones con descuento: ' + str(rec_desc))