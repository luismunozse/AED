'''
12. Cartas de Truco
Desarrollar un programa que genere al azar tres cartas simulando una mano de truco. A continuación deberá:

   1) Informar si entre las cartas se encuentra el as de espadas

   2) Verificar si las tres cartas son del mismo palo. Si es así, identificar cuál fue la mayor carta. En caso contrario,
    informarlo.
'''

import random

palos = ('oro','basto','espada','copa')
numeros = (1,2,3,4,5,6,7,8,9,10,11,12)

carta1 = random.choice(numeros), random.choice(palos)
carta2 = random.choice(numeros), random.choice(palos)
carta3 = random.choice(numeros), random.choice(palos)

print('Cartas asginadas: ')
print(carta1,carta2,carta3)

if carta1 == (1,'espada') or carta2 == (1,'espada') or carta3 == (1,'espada'):
    print('En su mano tiene el AS de Espadas')
else:
    print('No posse el AS de Espadas')

if carta1[1] == carta2[1] and carta1[1] == carta3[1]:
    print('Las cartas son del mismo palo')
    mayor_carta = max(carta1[0],carta2[0],carta3[0])
    print('La mayor carta es: ' + str(mayor_carta))
else:
    print('Al menos una carta es de distinto palo')