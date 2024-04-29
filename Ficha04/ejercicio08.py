'''
8. Lanzamiento de dados
Simular un juego en el que se lanzan dos dados.

 Si ambos dados son iguales o la suma entre ellos es impar, gana el usuario. En caso contrario, gana la máquina.
'''

import random

caras_dado = (1,2,3,4,5,6)
dado1 = random.choice(caras_dado)
dado2 = random.choice(caras_dado)
suma = dado1 + dado2

opcion = int(input('Bienvenido al juego. Presione una opcion para continuar (1-Jugar 2-Salir): '))

if opcion == 2:
    print('Adios!')
else:
    print('Tirando dados')
    print('Resultados: ' + '\nDado1: ' + str(dado1) + '\nDado2: ' + str(dado2))
    if(dado1 == dado2 or (suma % 2) != 0):
        print('Felicidades. Ganaste!')
    else:
        print('Lo siento. Perdiste!')
