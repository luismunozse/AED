'''
9. Costos del Proyecto
Una pequeña empresa de informática tiene que desarrollar un sistema de información y para ello tiene un presupuesto
de x pesos para cubrir los costos de crear el sistema. Sabiendo que tiene pensado ganar al menos 17% por el proyecto,
determine cuál es el valor máximo que pueden alcanzar los costos del proyecto.
'''

presupuesto = float(input('Ingrese el presupuesto en pesos: '))

ganancia_minima = presupuesto * 0.17

costo_maximo = presupuesto + ganancia_minima

print('El valor máximo que pueden alcanzar los costos del proyecto es: ', costo_maximo)