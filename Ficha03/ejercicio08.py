'''
8. Calculo Distancia de Viaje
Un persona cautivada por los paisajes argentinos se le ocurrió la loca idea de unir los puntos mas extremos
(Ushuahia y La Quiaca) en bicicleta, es decir se propuso hacer 3641.3 Km en bicicleta.

Nuestro aventurero efectivamente inició la travesía pero se accidentó y sólo recorrió x metros según su GPS.

Usted debe solicitar ese valor x e informar cuántos kilómetros y metros recorrió nuestro aventurero y qué
porcentaje represento lo recorrido del total de kms a recorrer de Ushuahia a La Quiaca (para el porcentaje usted
deberá realizar los calculos en metros).
'''

print('*' * 65)
print(' Cálculo Distancia de viaje ')
print('*' * 65)

recorrido = float(input('Ingrese la cantidad de kms recorridos: '))

total = 3641.3 * 1000

recorrido_metros = recorrido * 1000

porc_recorrido = (recorrido_metros * 100) / total

print('Recorrido ingresado: ', recorrido, 'kms')
print('Ud recorrió: ', recorrido_metros, 'metros')
print('Representa el ', porc_recorrido, '% del camino')