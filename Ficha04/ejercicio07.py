'''
7. Tirada de moneda
Programar una tirada de una moneda (opciones: cara o cruz) aleatoriamente. Permitir que un jugador apueste a cara o
cruz y luego informar si acertó o no con su apuesta.
'''

import random

opciones_tirada = ('cara', 'cruz')
tirada_jugador = input('Escriba la opcion elegida (cara o cruz): ')
tirada_pc = random.choice(opciones_tirada)

if tirada_jugador == tirada_pc:
    print('El jugador acertó')
else:
    print('Suerte para la proxima')
