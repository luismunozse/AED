'''
8. Rinde de un Campo Agricola
Un productor agricola desea saber cuantos quintales de trigo puede producir en su parcela. Se pide ingresar el largo
y el ancho en metros de la parcela y determinar el rinde sabiendo que en 10 m2 se obtienen 2 quintales.
'''

largo = float(input('Ingrese el largo de la parcela(en metros): '))
ancho = float(input('Ingrese el ancho de la parcela(en metros): '))

area_parcela = largo*ancho

rinde = area_parcela/5

print('La parcela puede producir: ', rinde, 'quintales')